# Task 06 – Netflix Business Insights Dashboard

## Project Overview

This project develops an end-to-end Data Science Business Insights Dashboard using Netflix content data.

It combines Exploratory Data Analysis (EDA), Machine Learning, interactive data visualization, and business recommendations to analyze Netflix's content catalog and extract meaningful insights.

An interactive dashboard is developed using **Streamlit and Plotly**, allowing users to explore content distribution, geographic patterns, genre representation, release trends, and machine learning results.

## Objectives

- Perform comprehensive exploratory data analysis.
- Identify patterns and trends in Netflix content.
- Develop and evaluate a Machine Learning classification model.
- Create interactive visualizations and dashboard filters.
- Generate meaningful business insights and recommendations.
- Present analytical findings through a professional business report.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive visualizations |
| Scikit-learn | Machine Learning |
| Streamlit | Interactive dashboard |
| Joblib | Model persistence |

## Dataset

**Dataset:** Netflix Movies and TV Shows

**Source:** Cleaned dataset generated in Task 1 – Data Cleaning.

**Dataset location:**

`Task-01-Data-Cleaning/data/processed/netflix_cleaned.csv`

The project reuses the cleaned dataset from Task 1 instead of maintaining a duplicate copy.

**Dataset overview:**
- Total records: 8,790
- Movies: 6,126
- TV Shows: 2,664
- Distinct country names: 85
- Release-year range: 1925–2021

## Project Structure

```text
Task-06-Business-Insights-Dashboard/
│
├── app.py
├── README.md
├── requirements.txt
│
├── assets/
│   └── dashboard_screenshot.png
│
├── notebooks/
│   └── business_analysis.ipynb
│
├── outputs/
│   ├── netflix_classification_model.pkl
│   ├── classification_report.csv
│   └── confusion_matrix.csv
│
├── reports/
│   └── business_insights_report.md
│
└── src/
    ├── __init__.py
    ├── analysis.py
    ├── business_insights.py
    ├── model.py
    └── visualizations.py
```

*Note: Generated output files appear after running the model evaluation. The notebook and screenshot can be added as project documentation.*

## Key Features

### 1. Executive Overview

Displays important business metrics:
- Total Netflix titles.
- Total Movies.
- Total TV Shows.
- Number of represented countries.

### 2. Interactive Content Analysis

- Movie vs TV Show distribution.
- Yearly content addition trends.
- Country-wise content distribution.
- Genre-wise content distribution.
- Content rating analysis.
- Release-year trends.
- Movie