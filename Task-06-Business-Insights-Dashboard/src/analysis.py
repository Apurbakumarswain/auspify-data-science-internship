
import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. DATASET PATH
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

REPO_ROOT = PROJECT_ROOT.parent

DATA_PATH = (
    REPO_ROOT
    / "Task-01-Data-Cleaning"
    / "data"
    / "processed"
    / "netflix_cleaned.csv"
)


# --------------------------------------------------
# 2. LOAD DATASET
# --------------------------------------------------

def load_data():

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    return df


# --------------------------------------------------
# 3. KEY BUSINESS METRICS
# --------------------------------------------------

def get_kpi_metrics(df):

    total_titles = len(df)

    total_movies = (df["type"] == "Movie").sum()

    total_tv_shows = (df["type"] == "TV Show").sum()

    total_countries = (
        df["country"]
        .str.split(",")
        .explode()
        .str.strip()
        .replace("Not Available", pd.NA)
        .dropna()
        .nunique()
    )

    movie_percentage = (
        total_movies / total_titles * 100
        if total_titles else 0
    )

    tv_percentage = (
        total_tv_shows / total_titles * 100
        if total_titles else 0
    )

    return {
        "total_titles": total_titles,
        "total_movies": int(total_movies),
        "total_tv_shows": int(total_tv_shows),
        "total_countries": int(total_countries),
        "movie_percentage": round(movie_percentage, 2),
        "tv_percentage": round(tv_percentage, 2)
    }


# --------------------------------------------------
# 4. CONTENT TYPE DISTRIBUTION
# --------------------------------------------------

def get_content_distribution(df):

    return (
        df["type"]
        .value_counts()
        .reset_index()
        .rename(columns={
            "type": "Content Type",
            "count": "Count"
        })
    )


# --------------------------------------------------
# 5. YEARLY CONTENT ADDITIONS
# --------------------------------------------------

def get_yearly_additions(df):

    yearly_data = (
        df.groupby(["date_added_year", "type"])
        .size()
        .reset_index(name="Total Titles")
    )

    return yearly_data


# --------------------------------------------------
# 6. COUNTRY-WISE CONTENT DISTRIBUTION
# --------------------------------------------------

def get_country_distribution(df):

    country_data = (
        df.assign(
            country=df["country"].str.split(",")
        )
        .explode("country")
    )

    country_data["country"] = (
        country_data["country"].str.strip()
    )

    country_data = country_data[
        ~country_data["country"].isin(["", "Not Available"])
    ]

    country_data = country_data[
        country_data["country"] != ""
    ]

    result = (
        country_data.groupby("country")
        .size()
        .reset_index(name="Total Titles")
        .sort_values("Total Titles", ascending=False)
    )

    return result.head(15)


# --------------------------------------------------
# 7. GENRE DISTRIBUTION
# --------------------------------------------------

def get_genre_distribution(df):

    genre_data = (
        df.assign(
            genre=df["listed_in"].str.split(",")
        )
        .explode("genre")
    )

    genre_data["genre"] = genre_data["genre"].str.strip()

    result = (
        genre_data.groupby("genre")
        .size()
        .reset_index(name="Total Titles")
        .sort_values("Total Titles", ascending=False)
    )

    return result.head(15)


# --------------------------------------------------
# 8. CONTENT RATING DISTRIBUTION
# --------------------------------------------------

def get_rating_distribution(df):

    result = (
        df["rating"]
        .value_counts()
        .reset_index()
        .rename(columns={
            "rating": "Content Rating",
            "count": "Total Titles"
        })
    )

    return result


# --------------------------------------------------
# 9. RELEASE YEAR TRENDS
# --------------------------------------------------

def get_release_year_trends(df):

    result = (
        df.groupby(["release_year", "type"])
        .size()
        .reset_index(name="Total Titles")
    )

    return result


# --------------------------------------------------
# 10. MOVIE DURATION ANALYSIS
# --------------------------------------------------

def get_movie_duration_analysis(df):

    movies = df[df["type"] == "Movie"].copy()

    result = (
        movies["duration_value"]
        .dropna()
        .describe()
        .round(2)
    )

    return result
