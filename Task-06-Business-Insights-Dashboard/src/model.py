
import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# --------------------------------------------------
# 1. PATH CONFIGURATION
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 2. TRAIN MODEL
# --------------------------------------------------

def train_classification_model(df):

    numerical_features = [
        "release_year",
        "date_added_year",
        "date_added_month"
    ]

    categorical_features = [
        "rating",
        "country",
        "listed_in"
    ]

    features = numerical_features + categorical_features

    X = df[features].copy()

    y = df["type"]

    # Separate numerical and categorical preprocessing

    numerical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(
            strategy="most_frequent"
        )),
        ("encoder", OneHotEncoder(
            handle_unknown="ignore"
        ))
    ])

    preprocessor = ColumnTransformer([
        ("num", numerical_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)
    ])

    # Complete machine learning pipeline

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(
            max_iter=1000,
            random_state=42
        ))
    ])

    # Train-test split

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Train

    model.fit(X_train, y_train)

    # Predict

    predictions = model.predict(X_test)

    # Evaluate

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(
        y_test,
        predictions,
        output_dict=True,
        zero_division=0
    )

    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=model.classes_
    )

    # Save model

    model_path = OUTPUT_DIR / "netflix_classification_model.pkl"

    joblib.dump(model, model_path)

    # Save evaluation results

    pd.DataFrame(report).transpose().to_csv(
        OUTPUT_DIR / "classification_report.csv"
    )

    pd.DataFrame(
        matrix,
        index=model.classes_,
        columns=model.classes_
    ).to_csv(
        OUTPUT_DIR / "confusion_matrix.csv"
    )

    return {
        "model": model,
        "accuracy": accuracy,
        "report": report,
        "confusion_matrix": matrix,
        "classes": model.classes_,
        "X_test": X_test,
        "y_test": y_test,
        "predictions": predictions
    }
