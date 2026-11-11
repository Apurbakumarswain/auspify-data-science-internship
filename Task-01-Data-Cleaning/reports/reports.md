# Task 01 – Netflix Data Cleaning and Preprocessing Report

## 1. Objective

The objective of this task was to clean and preprocess the Netflix Movies and TV Shows dataset using Python and Pandas, making it suitable for further data analysis.

## 2. Dataset Overview

| Attribute | Details |
|---|---|
| Dataset | Netflix Movies and TV Shows |
| Original records | 8,790 |
| Original columns | 10 |
| Final records | 8,790 |
| Final columns | 15 |

## 3. Methodology

The following operations were performed:

1. Imported the dataset using Pandas.
2. Inspected data types, missing values, duplicate records, and empty strings.
3. Identified placeholder values in the director and country columns.
4. Standardized `Not Given` to `Not Available`.
5. Converted `date_added` into datetime format.
6. Extracted numerical duration values and duration units.
7. Standardized `Seasons` to `Season`.
8. Extracted year, month, and month name from the date column.
9. Removed leading and trailing whitespace from text columns.
10. Exported the cleaned dataset into CSV format.

## 4. Results

| Data Quality Metric | Result |
|---|---:|
| Original records | 8,790 |
| Final records | 8,790 |
| Final columns | 15 |
| Missing values | 0 |
| Duplicate records | 0 |
| Movie duration records | 6,126 |
| TV Show duration records | 2,664 |

The original dataset contained no missing values or duplicate records. Therefore, no records were removed for these reasons.

## 5. Deliverables

- Jupyter Notebook: `notebooks/netflix_data_cleaning.ipynb`
- Python script: `src/clean_data.py`
- Cleaned dataset: `data/processed/netflix_cleaned.csv`
- Project documentation: `README.md`

## 6. Conclusion

The Netflix dataset was successfully cleaned and transformed using Pandas. Additional duration and date-related features were created, and the final dataset was exported successfully.

A reusable Python script was also developed to automate the cleaning process.

The resulting dataset is ready for further exploratory data analysis.

## 7. Technologies

Python, Pandas, NumPy, Jupyter Notebook, VS Code, Git, and GitHub.

---

**Internship:** Auspify Data Science Internship  
**Task:** 01 – Data Cleaning and Preprocessing