# StateDrugUtilizationAnalysis
## Project Overview

This project examines inefficiencies in the **Medicaid State Drug Utilisation Review Program (SDUR)** using data analysis and visualisation. The key objective is to uncover patterns of wasteful spending and offer insights that can inform healthcare policy improvements.

By analysing prescription drug data across U.S. states, we found:

* 💸 **Smaller package sizes are disproportionately costly and inefficient**.
* 🏥 **Certain states are nearly 100% dependent on Medicaid** for drug coverage, highlighting socioeconomic challenges.
* ⚖️ These findings emphasise the need for **employment-driven health benefits** and smarter drug distribution strategies.

---

## Project Structure

| Folder/File                   | Description                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------- |
| `DataCollection.py`           | Python script to **automatically download SDUD data** and upload it to a Snowflake warehouse.     |
| `Text files`                  | SQL queries written and executed in **Snowflake** for data wrangling, cleaning, and aggregations. |
| `PowerBI_Dashboard.pbix`      | Interactive **Power BI dashboard** to visualize insights from the analyzed data.                  |
| `README.md`                   | You're reading it!                                                                                |

---

## How It Works

1. **Data Ingestion**

   * The Python script uses the CMS Medicaid URL to download the latest SDUD data.
   * Data is uploaded to **Snowflake** cloud data warehouse.

2. **Data Analysis**

   * SQL queries are executed in Snowflake to:

     * Classify package sizes (e.g., Small vs. Large).
     * Identify outliers in spending.
     * Compare Medicaid dependence by state.

3. **Data Visualization**

   * Snowflake tables are connected to **Power BI**.
   * Dynamic visuals and KPIs are designed to present:

     * Cost% % by package size.
     * State-wise Medicaid reliance.
     * Top drugs by reimbursement.

---

## Technologies Used

* **Python** (for automated data download)
* **Snowflake** (data warehouse and SQL analysis)
* **Power BI** (dashboard visualization)
* **DAX** (Power BI calculations)

---

## Key Insights

* **Small packages** often contribute a **disproportionately high Medicaid cost**, suggesting inefficiency.
* **Some states show 100% reliance on Medicaid** for drug coverage, indicating lack of employer-backed insurance.
* These patterns reflect both economic and healthcare challenges, emphasizing the importance of targeted intervention.

### Dependencies

* Python 3.x
* `pandas`, `requests`, `snowflake-connector-python`
* Snowflake account
* Power BI Desktop

### Steps to Reproduce

1. Run `DataCollection.py` to load data into your Snowflake account.
2. Use the Snowflake SQL Worksheet to clean and analyze the data.
3. Connect Power BI to your Snowflake data source to use the provided `.pbix` dashboard template.

---

## 📁 Data Source

* [CMS Medicaid State Drug Utilization Data](https://data.medicaid.gov/)

---

## 🤝 Contribution

Ideas, feedback, and forks are welcome. This project is a work-in-progress and open for collaboration, especially in the areas of:

* Automating Power BI publishing
* Advanced DAX calculations
* Policy recommendations based on findings


## 📄 License

This project is shared for educational and non-commercial purposes.


##Website: https://victorious-bougon-37a.notion.site/State-Drug-Utilization-Program-Analysis-20d11f4de15980f2a7eed13e4bc19fcd?pvs=74
