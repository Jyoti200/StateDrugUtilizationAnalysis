import os
import requests
import pandas as pd
import snowflake.connector
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

DATA_URL = 'https://download.medicaid.gov/data/SDUD-2024.csv'  
LOCAL_CSV = 'SDUD-2024.csv'
TABLE_NAME = "SUD"
STAGE_NAME = "MYSTAGE"
# Download the CSV from data.gov.in 
response = requests.get(DATA_URL)
with open(LOCAL_CSV, 'wb') as f:
    f.write(response.content)

print("Data downloaded from data.gov.in")

#Preview the data and load into Pandas ---
df = pd.read_csv(LOCAL_CSV)
print("Preview of DataFrame:")
print(df.head())

#Connect to Snowflake ---
conn = snowflake.connector.connect(
    USER=os.environ['USER'],
    PASSWORD=os.environ['PASSWORD'],
    ACCOUNT=os.environ['ACCOUNT'],
    WAREHOUSE=os.environ['WAREHOUSE'],
    DATABASE=os.environ['DATABASE'],
    SCHEMA=os.environ['SCHEMA']
)


cursor = conn.cursor()

# === Drop and create table ===
cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
columns_sql = ", ".join([f'"{col}" STRING' for col in df.columns])
cursor.execute(f"CREATE TABLE {TABLE_NAME} ({columns_sql})")
print("Table created in Snowflake")

# === Create stage ===
cursor.execute(f"CREATE OR REPLACE STAGE {STAGE_NAME}")
print("Stage created")

# === Upload CSV ===
put_command = f'''
snowsql -a {ACCOUNT} -u {USER} -p {PASSWORD} -d {DATABASE} -s {SCHEMA} -w {WAREHOUSE} -q "PUT file://{os.path.abspath(LOCAL_CSV)} @{STAGE_NAME} OVERWRITE = TRUE"
'''
subprocess.run(put_command, shell=True, check=True)
print("CSV uploaded to stage")

# === Copy into table ===
copy_sql = f"""
COPY INTO {TABLE_NAME}
FROM @{STAGE_NAME}
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1)
"""
cursor.execute(copy_sql)
print("Data copied from stage to table")

#Done
cursor.close()
conn.close()
print("Data pipeline complete!")