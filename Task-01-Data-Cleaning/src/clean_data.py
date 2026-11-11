
from pathlib import Path
import pandas as pd


# 1. Define project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_DIR / "data" / "raw" / "Dataset.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "processed" / "netflix_cleaned.csv"


def clean_netflix_data():

    # 2. Load the original dataset
    df = pd.read_csv(RAW_FILE)

    print("Original Dataset Shape:", df.shape)

    # 3. Remove unwanted spaces from text columns
    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # 4. Replace placeholder values
    df["director"] = df["director"].replace("Not Given", "Not Available")
    df["country"] = df["country"].replace("Not Given", "Not Available")

    # 5. Convert date column into datetime format
    df["date_added"] = pd.to_datetime(
        df["date_added"], errors="coerce"
    )

    # 6. Extract numerical duration and its unit
    df["duration_value"] = pd.to_numeric(
        df["duration"].str.extract(r"(\d+)")[0],
        errors="coerce"
    ).astype("Int64")

    df["duration_unit"] = df["duration"].str.extract(
        r"([A-Za-z]+)$"
    )[0]

    df["duration_unit"] = df["duration_unit"].replace(
        {"Seasons": "Season"}
    )

    # 7. Extract date-related features
    df["date_added_year"] = df["date_added"].dt.year
    df["date_added_month"] = df["date_added"].dt.month
    df["date_added_month_name"] = df["date_added"].dt.month_name()

    # 8. Validate the cleaned dataset
    print("\n--- Data Quality Report ---")
    print("Final Dataset Shape:", df.shape)
    print("Total Missing Values:", df.isnull().sum().sum())
    print("Duplicate Records:", df.duplicated().sum())

    print("\nMissing Values by Column:")
    print(df.isnull().sum())

    print("\nDuration Unit Counts:")
    print(df["duration_unit"].value_counts())

    # 9. Save the cleaned dataset
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nCleaned dataset saved successfully!")
    print("Output location:", OUTPUT_FILE)


# 10. Run the program
if __name__ == "__main__":
    clean_netflix_data()
