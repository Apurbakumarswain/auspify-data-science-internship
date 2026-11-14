# Task 02 – Exploratory Data Analysis (EDA) on Netflix Dataset

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on the Netflix Titles dataset to discover meaningful patterns, trends, and insights.

The analysis explores content distribution, country-wise representation, popular categories, release years, content ratings, durations, and Netflix content addition trends.

## Objectives

- Understand the structure and statistical properties of the dataset.
- Analyze the distribution of Movies and TV Shows.
- Identify the top countries and content categories.
- Explore yearly and monthly content addition trends.
- Analyze movie durations and TV show seasons.
- Visualize important findings using charts.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

## Project Structure

```text
Task-02-Exploratory-Data-Analysis/
│
├── notebooks/
│   └── netflix_eda.ipynb
│
├── reports/
│   └── eda_report.md
│
├── screenshots/
│
├── visualizations/
│   ├── content_distribution.png
│   ├── top_10_countries.png
│   ├── top_10_categories.png
│   ├── yearly_content_trend.png
│   ├── average_duration_analysis.png
│   ├── release_year_trend.png
│   ├── content_rating_distribution.png
│   └── monthly_content_additions.png
│
└── README.md
```

## Dataset Information

- Total Records: 8,790
- Total Features: 15
- Missing Values: 0
- Duplicate Records: 0

The cleaned dataset generated in Task 1 was used for this analysis.

## Key Findings

1. Movies account for approximately 69.69% of the dataset, while TV Shows account for 30.31%.
2. The United States has the highest number of country-title associations, followed by India.
3. International Movies and Dramas are the most frequently represented categories.
4. Netflix content additions peaked in 2019, with 2,016 titles.
5. The average movie duration is approximately 99.58 minutes.
6. TV Shows have an average of approximately 1.75 seasons.
7. TV-MA is the most common content rating.
8. July has the highest number of content additions among the months.

## Visualizations

Eight visualizations were created using Matplotlib and Seaborn and saved in the `visualizations` directory.

## Detailed Report

For methodology, detailed findings, and limitations, refer to:

`reports/eda_report.md`

## How to Run

1. Clone this repository.
2. Open the project in VS Code.
3. Install the required libraries if they are not already installed:

```bash
python -m pip install pandas numpy matplotlib seaborn jupyter
```

4. Open `notebooks/netflix_eda.ipynb`.
5. Select your Python kernel.
6. Run the notebook cells from top to bottom.

Ensure the cleaned dataset from Task 1 is available at:

`Task-01-Data-Cleaning/data/processed/netflix_cleaned.csv`

## Skills Demonstrated

- Exploratory Data Analysis
- Data Wrangling
- Statistical Analysis
- Data Visualization
- Data Interpretation
- Python and Pandas

---

**Internship:** Auspify Data Science Internship  
**Task:** Task 02 – Exploratory Data Analysis
