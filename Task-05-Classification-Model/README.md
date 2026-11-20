# Task 05 – Machine Learning Classification Model

## Project Overview
This project develops machine learning classification models to predict whether a Netflix title is a Movie or TV Show based on available dataset features.

## Objectives
- Select and prepare relevant features.
- Split data into training and testing datasets.
- Train classification algorithms.
- Evaluate model performance.
- Compare model accuracy.

## Dataset
- Dataset: Netflix Movies and TV Shows
- Total records: 8,790
- Source: Cleaned dataset generated in Task 1.
- Target variable: `type`

## Features Used
**Numerical Features**
- release_year
- date_added_year
- date_added_month

**Categorical Features**
- rating
- country
- listed_in

The `duration` and `duration_unit` columns were excluded to avoid direct target leakage.

## Machine Learning Algorithms
1. Logistic Regression
2. Random Forest Classifier

## Data Preparation
- Train-test split: 80:20
- Random state: 42
- Stratified sampling
- Missing value imputation
- One-Hot Encoding
- Standard Scaling

## Model Evaluation

| Model | Accuracy |
|---|---:|
| Logistic Regression | 99.26% |
| Random Forest | 96.99% |

Logistic Regression achieved the highest accuracy on the test dataset.

## Evaluation Metrics
The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Key Findings
- Both models successfully classified Netflix content.
- Logistic Regression achieved 99.26% accuracy.
- Random Forest achieved 96.99% accuracy.
- Logistic Regression performed better on the selected test dataset.

## Output Files
The `outputs` folder contains:
- `model_comparison.csv`
- `prediction_results.csv`
- `logistic_regression_report.csv`
- `random_forest_report.csv`
- `logistic_confusion_matrix.csv`
- `random_forest_confusion_matrix.csv`
- `logistic_regression_model.pkl`
- `random_forest_model.pkl`

## Conclusion
This project demonstrates the application of supervised machine learning classification algorithms to Netflix content data.

Logistic Regression achieved the highest test accuracy among the two evaluated models. Further validation on unseen and newer data is recommended before using the model for real-world predictions.

## Skills Demonstrated
- Machine Learning
- Classification Algorithms
- Feature Selection
- Data Preprocessing
- Scikit-Learn
- Model Training
- Model Evaluation
- Predictive Analytics