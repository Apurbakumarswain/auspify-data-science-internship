# Task 04 – Trend Prediction Analysis

## Project Overview
This project analyzes historical Netflix content release trends and applies forecasting techniques to estimate future content trends.

The analysis uses Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

## Objectives
- Analyze historical Netflix content release patterns.
- Calculate yearly content counts.
- Visualize content trends over time.
- Build forecasting models.
- Evaluate model performance.
- Generate future predictions for 2022–2026.

## Dataset
- Dataset: Netflix Movies and TV Shows
- Total records: 8,790
- Source: Cleaned dataset generated in Task 1.
- Target variable: Yearly content count grouped by release year.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Models Implemented

### 1. Linear Regression
Used to identify a linear relationship between release year and yearly content count and generate future predictions.

### 2. Naive Forecast
Uses the previous observed year's content count as the prediction for the next year.

## Model Evaluation

The models were evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

| Model | MAE | MSE | RMSE |
|---|---:|---:|---:|
| Linear Regression | 380.66 | 174719.57 | 417.99 |
| Naive Forecast | 159.80 | 35960.60 | 189.63 |

The Naive Forecast model achieved lower errors across all three evaluation metrics on the test period.

## Key Findings
- Historical Netflix content release trends were analyzed.
- Linear Regression and Naive Forecast models were compared.
- The Naive Forecast model performed better on the selected test period.
- Future predictions were generated for 2022–2026.

## Output Files
The `outputs` folder contains:

- `yearly_content_trends.csv`
- `model_comparison.csv`
- `future_predictions.csv`

## Project Structure
```text
Task-04-Trend-Prediction-Analysis/
│
├── notebooks/
│   └── trend_prediction.ipynb
│
├── outputs/
│   ├── yearly_content_trends.csv
│   ├── model_comparison.csv
│   └── future_predictions.csv
│
├── screenshots/
├── README.md
└── requirements.txt
```

## Conclusion
This project demonstrates how historical data can be analyzed to identify trends and build forecasting models. The Naive Forecast model outperformed Linear Regression on the selected test dataset.

**Limitation:** These forecasts concern the release-year distribution of titles in the available Netflix dataset. They should not be interpreted as direct predictions of Netflix's future content acquisitions.

## Skills Demonstrated
- Time Series Analysis
- Data Visualization
- Forecasting Techniques
- Linear Regression
- Model Evaluation
- Predictive Analytics