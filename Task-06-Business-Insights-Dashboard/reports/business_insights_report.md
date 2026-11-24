# Netflix Business Insights Report

## 1. Executive Summary

This project presents an end-to-end data science analysis of Netflix's content catalog. It combines exploratory data analysis, interactive visualizations, machine learning classification, and business recommendations.

The objective is to understand the composition of Netflix's catalog, identify content distribution patterns, and demonstrate how data science techniques can support content strategy decisions.

The analysis uses a cleaned dataset containing **8,790 Netflix titles**.

## 2. Dataset Overview

- Total records: 8,790
- Movies: 6,126
- TV Shows: 2,664
- Distinct country names associated with titles: 85
- Release-year range: 1925–2021

The dataset includes content type, title, director, country, release year, rating, duration, genre, and date-added information.

## 3. Exploratory Data Analysis

### 3.1 Content Distribution

- Movies account for approximately 69.69% of the catalog.
- TV Shows account for approximately 30.31%.

**Observation:** Movies form the larger share of the Netflix catalog in this dataset.

### 3.2 Geographic Distribution

The United States is the most represented country, with 3,240 title-country associations.

**Observation:** The United States has the highest representation in the dataset. Country associations do not necessarily indicate exclusive production origin because a title can be associated with multiple countries.

### 3.3 Genre Analysis

The most represented genre is International Movies, with 2,752 titles.

Other highly represented categories include:
- Dramas
- Comedies
- International TV Shows
- Documentaries
- Action & Adventure

**Observation:** International Movies and Dramas have substantial representation in the catalog.

### 3.4 Content Addition Trends

The dataset records 1,498 titles added in 2021, compared with 1,879 in 2020.

This represents an approximate decrease of 20.28%.

**Observation:** The number of titles added in 2021 was lower than in 2020. This comparison describes the available dataset and should not be interpreted as a complete measure of Netflix's actual acquisition activity.

### 3.5 Movie Duration Analysis

- Average movie duration: 99.58 minutes
- Median movie duration: 98 minutes

**Observation:** The average and median durations are relatively close, suggesting that the typical movie duration is around 100 minutes.

## 4. Machine Learning Model

### 4.1 Objective

A classification model was developed to predict whether a Netflix title is a Movie or a TV Show using available catalog features.

### 4.2 Features Used

**Numerical features:**
- Release year
- Date-added year
- Date-added month

**Categorical features:**
- Rating
- Country
- Listed genre

**Target variable:** Content type (Movie or TV Show).

Duration-related features were excluded to avoid directly encoding the target through movie and TV Show duration conventions.

### 4.3 Data Preparation

The following preprocessing techniques were applied:

- Median imputation for numerical features.
- Standard scaling for numerical features.
- Most-frequent imputation for categorical features.
- One-hot encoding for categorical variables.
- Stratified train-test split.

The dataset was divided into 80% training data and 20% testing data.

### 4.4 Model Performance

**Algorithm:** Logistic Regression

**Test accuracy:** 99.26%

| Metric | Movie | TV Show |
|---|---:|---:|
| Precision | 99.27% | 99.24% |
| Recall | 99.67% | 98.31% |
| F1-score | 99.47% | 98.78% |

**Confusion Matrix:**

| Actual / Predicted | Movie | TV Show |
|---|---:|---:|
| Movie | 1,221 | 4 |
| TV Show | 9 | 524 |

The model correctly classified 1,745 out of 1,758 test records.

**Interpretation:** The Logistic Regression model achieved high classification performance on the held-out test set.

However, this model classifies existing catalog records. It does not predict viewer preferences, revenue, popularity, or future content demand. Its high accuracy should also be interpreted in light of the strong associations between catalog metadata and content type.

## 5. Business Insights and Recommendations

Based on the analysis, the following recommendations are proposed:

### Recommendation 1: Evaluate Content Balance

Movies represent approximately 69.69% of the catalog. Netflix could evaluate whether its content mix aligns with viewer engagement and strategic objectives.

### Recommendation 2: Explore Geographic Opportunities

The United States has the highest representation in the dataset. Regional catalog representation can be compared with actual audience engagement before making investment decisions.

### Recommendation 3: Review Genre Representation

International Movies is the most represented genre. Content planners could compare genre representation with viewing performance to identify potential catalog gaps.

### Recommendation 4: Monitor Content Addition Trends

The decrease in recorded additions between 2020 and 2021 highlights the importance of monitoring yearly catalog changes when planning content strategy.

### Recommendation 5: Study Movie Duration Patterns

The average movie duration is approximately 100 minutes. Viewer completion rates and engagement data could help determine whether content length influences audience experience.

## 6. Interactive Dashboard

A Streamlit dashboard was developed to present the analysis in an interactive format.

**Dashboard features:**
- Executive KPI overview.
- Movie and TV Show distribution.
- Yearly content addition trends.
- Geographic distribution analysis.
- Genre distribution analysis.
- Content rating analysis.
- Release-year trends.
- Movie duration analysis.
- Interactive content-type and release-year filters.
- Machine learning model evaluation.
- Business insights and recommendations.

Plotly was used to create interactive charts, while Streamlit provides the dashboard interface.

## 7. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit
- Joblib

## 8. Limitations

This project uses catalog metadata and does not include actual viewer-level information.

Therefore:
- The analysis cannot establish actual viewer preferences.
- Country and genre representation do not establish commercial success.
- Content addition trends do not necessarily represent acquisition decisions.
- The classification model does not forecast future demand or profitability.
- Business recommendations should be validated using viewership, engagement, and revenue data before implementation.

## 9. Conclusion

This project demonstrates an end-to-end data science workflow, from data analysis and preprocessing to machine learning, interactive dashboard development, and business recommendations.

The Streamlit dashboard provides an accessible way to explore Netflix catalog patterns, while the Logistic Regression model demonstrates how machine learning can classify content using catalog metadata.

Overall, the project showcases practical applications of data science, predictive analytics, data visualization, and business storytelling.
