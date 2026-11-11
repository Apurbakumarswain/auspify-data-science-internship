# Task 01: Netflix Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing the Netflix Movies and TV Shows dataset using Python and Pandas.

The objective is to improve data quality, standardize inconsistent values, transform date and duration columns, and prepare a structured dataset for further analysis.

## Dataset Information

- **Dataset:** Netflix Movies and TV Shows
- **Original Records:** 8,790
- **Original Columns:** 10
- **Final Records:** 8,790
- **Final Columns:** 15

The original dataset is stored locally in `data/raw/` and is excluded from GitHub.

## Technologies Used

- Python 3.11
- Pandas
- NumPy
- Jupyter Notebook
- VS Code
- Git and GitHub

## Project Structure

```text
Task-01-Data-Cleaning/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── netflix_cleaned.csv
│
├── notebooks/
│   └── netflix_data_cleaning.ipynb
│
├── src/
│   └── clean_data.py
│
├── reports/
├── screenshots/
└── README.md
```

## Data Cleaning and Preprocessing Steps

1. Loaded the Netflix dataset using Pandas.
2. Inspected dataset structure, data types, missing values, and duplicate records.
3. Checked for empty strings and placeholder values.
4. Standardized `Not Given` values in the director and country columns to `Not Available`.
5. Converted `date_added` into datetime format.
6. Extracted numerical duration values and standardized duration units.
7. Extracted date-related features:
   - `date_added_year`
   - `date_added_month`
   - `date_added_month_name`
8. Removed leading and trailing whitespace from text columns.
9. Validated the final dataset and exported it as a CSV file.

## Final Data Quality Results

| Metric | Result |
|---|---:|
| Total Records | 8,790 |
| Total Columns | 15 |
| Missing Values | 0 |
| Duplicate Records | 0 |
| Movie Duration Records | 6,126 |
| TV Show Duration Records | 2,664 |

**Note:** The original dataset contained no missing values or duplicate records. Placeholder values were standardized rather than treating them as missing records.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Apurbakumarswain/auspify-data-science-internship.git
```

### 2. Navigate to the project directory

```bash
cd auspify-data-science-internship
```

### 3. Install dependencies

```bash
pip install pandas numpy
```

### 4. Place the original dataset

Place `Dataset.csv` inside:

```text
Task-01-Data-Cleaning/data/raw/
```

### 5. Execute the cleaning script

```bash
python Task-01-Data-Cleaning/src/clean_data.py
```

The cleaned dataset will be generated at:

```text
Task-01-Data-Cleaning/data/processed/netflix_cleaned.csv
```

Alternatively, open and execute `notebooks/netflix_data_cleaning.ipynb` using Jupyter Notebook or VS Code.

## Project Deliverables

- Exploratory data inspection and cleaning notebook.
- Reusable Python data-cleaning script.
- Processed Netflix dataset.
- Project documentation.

## Learning Outcomes

- Data inspection and quality assessment.
- Handling inconsistent and placeholder values.
- Date and duration feature engineering.
- Data transformation using Pandas.
- Reproducible data-cleaning workflows.
- Git and GitHub project management.

---

**Internship:** Auspify Data Science Internship  
**Task:** 01 – Data Cleaning and Preprocessing