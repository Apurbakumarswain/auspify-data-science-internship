# Auspify Data Science Internship Portfolio

A collection of six data science projects completed as part of the **Auspify Data Science Internship**, using the Netflix Movies and TV Shows dataset.

The portfolio demonstrates a complete data science workflow — from data cleaning and exploratory analysis to recommendation systems, predictive modeling, and an interactive business insights dashboard.

## Internship Overview

**Organization:** Auspify  
**Domain:** Data Science  
**Programming Language:** Python  
**Dataset:** Netflix Movies and TV Shows

### Project Objectives

- Clean and preprocess real-world datasets.
- Perform exploratory data analysis and statistical analysis.
- Build a content-based recommendation system.
- Analyze historical trends and develop forecasting models.
- Train and evaluate machine learning classification models.
- Develop an interactive dashboard with actionable business insights.

## Projects Completed

| Task | Project | Main Technologies |
|---|---|---|
| 01 | Netflix Data Cleaning and Preprocessing | Python, Pandas, NumPy |
| 02 | Exploratory Data Analysis | Pandas, Matplotlib, Seaborn |
| 03 | Netflix Content Recommendation System | Pandas, Scikit-learn, TF-IDF |
| 04 | Trend Prediction Analysis | Pandas, Matplotlib, Scikit-learn |
| 05 | Machine Learning Classification Model | Scikit-learn, Pandas |
| 06 | Netflix Business Insights Dashboard | Streamlit, Plotly, Scikit-learn |

---

## Task Details

### Task 01 — Data Cleaning and Preprocessing

**Folder:** `Task-01-Data-Cleaning/`

Cleaned and transformed the Netflix dataset to prepare it for further analysis.

Key activities:
- Inspected dataset structure and data quality.
- Checked missing values and duplicate records.
- Standardized inconsistent and placeholder values.
- Converted date columns into datetime format.
- Extracted duration values and standardized duration units.
- Created date-related features.

**Results:**
- 8,790 records retained.
- 15 final columns.
- 0 missing values.
- 0 duplicate records.

### Task 02 — Exploratory Data Analysis

**Folder:** `Task-02-Exploratory-Data-Analysis/`

Explored the cleaned Netflix dataset to identify patterns, distributions, and trends.

Key activities:
- Movie and TV Show distribution analysis.
- Country-wise and genre-wise analysis.
- Content ratings and duration analysis.
- Yearly and monthly content addition trends.
- Data visualization using Matplotlib and Seaborn.

**Key findings:**
- Movies represent approximately 69.69% of the dataset.
- TV Shows represent approximately 30.31%.
- International Movies and Dramas are highly represented categories.
- The average movie duration is approximately 99.58 minutes.
- 2019 recorded 2,016 content additions in the analysis.

### Task 03 — Netflix Content Recommendation System

**Folder:** `Task-03-Recommendation-System/`

Developed a content-based recommendation system that suggests similar Netflix titles using metadata and categories.

Key activities:
- Feature extraction and text preprocessing.
- TF-IDF vectorization.
- Cosine similarity calculation.
- Top-five recommendation generation.
- Category-overlap evaluation.

**Evaluation result:**

The documented test using *Dick Johnson Is Dead* returned five recommendations, all matching the selected category criteria — a 100% category match rate.

This measures category overlap, not actual user satisfaction or recommendation accuracy.

### Task 04 — Trend Prediction Analysis

**Folder:** `Task-04-Trend-Prediction-Analysis/`

Analyzed historical Netflix content release-year patterns and compared forecasting approaches.

Models implemented:
- Linear Regression.
- Naive Forecast.

**Model comparison:**

| Model | MAE | MSE | RMSE |
|---|---:|---:|---:|
| Linear Regression | 380.66 | 174719.57 | 417.99 |
| Naive Forecast | 159.80 | 35960.60 | 189.63 |

The Naive Forecast achieved lower errors across all three evaluation metrics on the selected test period.

Future predictions were generated for 2022–2026.

**Note:** These forecasts concern the release-year distribution of titles in the available dataset. They are not direct predictions of future Netflix acquisitions.

### Task 05 — Machine Learning Classification Model

**Folder:** `Task-05-Classification-Model/`

Developed supervised machine learning models to classify Netflix titles as Movies or TV Shows.

Algorithms:
- Logistic Regression.
- Random Forest Classifier.

Methodology:
- Feature selection and preprocessing.
- Train-test split using stratified sampling.
- Missing-value imputation.
- One-Hot Encoding and Standard Scaling.
- Model evaluation using accuracy, precision, recall, F1-score, and confusion matrices.

**Model comparison:**

| Model | Accuracy |
|---|---:|
| Logistic Regression | 99.26% |
| Random Forest | 96.99% |

Logistic Regression achieved the higher accuracy on the selected test dataset.

### Task 06 — Netflix Business Insights Dashboard

**Folder:** `Task-06-Business-Insights-Dashboard/`

Developed an end-to-end interactive dashboard combining data analysis, machine learning, visualizations, and business recommendations.

Key features:
- Executive overview and KPI metrics.
- Interactive content distribution analysis.
- Yearly content addition trends.
- Country and genre analysis.
- Content rating analysis.
- Release-year trends.
- Movie duration analysis.
- Machine learning model evaluation.
- Business recommendations.
- Professional business insights report.

**Technologies:** Streamlit, Plotly, Pandas, NumPy, Scikit-learn, and Joblib.

The dashboard reuses the cleaned dataset from Task 1 instead of maintaining a duplicate dataset.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn |
| NLP and Recommendations | TF-IDF, Cosine Similarity |
| Dashboard | Streamlit |
| Model Persistence | Joblib |
| Development | VS Code, Jupyter Notebook |
| Version Control | Git, GitHub |

## Repository Structure

```text
Auspify-Data-Science-Internship/
│
├── Task-01-Data-Cleaning/
├── Task-02-Exploratory-Data-Analysis/
├── Task-03-Recommendation-System/
├── Task-04-Trend-Prediction-Analysis/
├── Task-05-Classification-Model/
├── Task-06-Business-Insights-Dashboard/
│
├── .gitignore
├── README.md
└── requirements.txt
```

Each task folder contains its own project files, documentation, and task-specific dependencies where applicable.

## Dataset Information

The projects use the **Netflix Movies and TV Shows** dataset.

The cleaned dataset generated in Task 1 is reused in subsequent projects.

Dataset location:

`Task-01-Data-Cleaning/data/processed/netflix_cleaned.csv`

The original raw dataset is excluded from version control.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Apurbakumarswain/auspify-data-science-internship.git
```

### 2. Navigate to the repository

```bash
cd auspify-data-science-internship
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run individual projects

Open the relevant task folder and follow its README instructions.

For the Task 6 interactive dashboard:

```bash
cd Task-06-Business-Insights-Dashboard
python -m streamlit run app.py
```

Ensure the cleaned dataset from Task 1 is available at the expected repository-relative location before running projects that depend on it.

## Screenshots and Project Outputs

Screenshots, visualizations, evaluation results, and generated outputs are organized within the respective task folders.

Explore each task's `screenshots/`, `outputs/`, and `visualizations/` directories where available.

## Important Notes and Limitations

- The recommendation system uses content metadata and category similarity, not user viewing history.
- Trend forecasts describe historical release-year distributions in the available dataset.
- Classification results are based on a selected train-test split and do not guarantee performance on future data.
- The business dashboard analyzes catalog representation; the dataset does not provide actual viewership, revenue, or audience engagement.
- Results should be interpreted within the limitations of the dataset and evaluation methods.

## Skills Demonstrated

- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Data Visualization and Storytelling
- Feature Engineering
- Recommendation Systems
- Natural Language Processing Fundamentals
- Predictive Analytics
- Machine Learning Classification
- Model Evaluation and Validation
- Interactive Dashboard Development
- Business Insights and Recommendations
- Git and GitHub

## Conclusion

This internship portfolio demonstrates the application of Python-based data science techniques across six practical projects.

Starting with raw data preparation, the work progresses through exploratory analysis, recommendation systems, forecasting, classification, and an interactive business insights dashboard.

Together, these projects demonstrate a practical understanding of the data science workflow, analytical problem-solving, machine learning, and communicating findings through visualizations and reports.

---

**Internship:** Auspify Data Science Internship  
**Portfolio:** Six completed data science projects  
**GitHub:** [Auspify Data Science Internship Repository](https://github.com/Apurbakumarswain/auspify-data-science-internship)