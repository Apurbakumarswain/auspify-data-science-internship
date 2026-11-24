
import pandas as pd


# --------------------------------------------------
# 1. CONTENT MIX INSIGHTS
# --------------------------------------------------

def content_mix_insights(df):

    counts = df["type"].value_counts()

    total = len(df)

    movie_pct = counts.get("Movie", 0) / total * 100
    tv_pct = counts.get("TV Show", 0) / total * 100

    return {
        "movie_percentage": round(movie_pct, 2),
        "tv_percentage": round(tv_pct, 2),
        "dominant_type": counts.idxmax()
    }


# --------------------------------------------------
# 2. TOP COUNTRY INSIGHT
# --------------------------------------------------

def top_country_insight(df):

    countries = (
        df.assign(country=df["country"].str.split(","))
        .explode("country")
    )

    countries["country"] = countries["country"].str.strip()

    countries = countries[
        ~countries["country"].isin(["", "Not Available"])
    ]

    counts = countries["country"].value_counts()

    return {
        "top_country": counts.index[0],
        "title_count": int(counts.iloc[0])
    }


# --------------------------------------------------
# 3. TOP GENRE INSIGHT
# --------------------------------------------------

def top_genre_insight(df):

    genres = (
        df.assign(genre=df["listed_in"].str.split(","))
        .explode("genre")
    )

    genres["genre"] = genres["genre"].str.strip()

    counts = genres["genre"].value_counts()

    return {
        "top_genre": counts.index[0],
        "title_count": int(counts.iloc[0])
    }


# --------------------------------------------------
# 4. CONTENT ADDITION TREND
# --------------------------------------------------

def content_addition_insight(df):

    yearly = (
        df.groupby("date_added_year")
        .size()
        .sort_index()
    )

    latest_year = int(yearly.index.max())

    latest_count = int(yearly.loc[latest_year])

    previous_year = latest_year - 1

    previous_count = int(yearly.get(previous_year, 0))

    if previous_count > 0:

        growth = (
            (latest_count - previous_count)
            / previous_count
        ) * 100

    else:
        growth = None

    return {
        "latest_year": latest_year,
        "latest_count": latest_count,
        "previous_year": previous_year,
        "previous_count": previous_count,
        "growth_percentage": (
            round(growth, 2)
            if growth is not None else None
        )
    }


# --------------------------------------------------
# 5. MOVIE DURATION INSIGHT
# --------------------------------------------------

def movie_duration_insight(df):

    movies = df[df["type"] == "Movie"]

    average_duration = movies["duration_value"].mean()

    median_duration = movies["duration_value"].median()

    return {
        "average_duration": round(average_duration, 2),
        "median_duration": round(median_duration, 2)
    }


# --------------------------------------------------
# 6. GENERATE BUSINESS RECOMMENDATIONS
# --------------------------------------------------

def generate_recommendations(df):

    mix = content_mix_insights(df)
    country = top_country_insight(df)
    genre = top_genre_insight(df)
    trend = content_addition_insight(df)
    duration = movie_duration_insight(df)

    recommendations = [
        (
            f"Content portfolio: Movies represent "
            f"{mix['movie_percentage']}% of the catalog. "
            f"Evaluate whether the existing Movie-TV Show "
            f"balance matches audience engagement and demand."
        ),

        (
            f"Geographic strategy: {country['top_country']} "
            f"has the highest number of catalog entries "
            f"({country['title_count']}). Investigate regional "
            f"audience demand and opportunities in other markets."
        ),

        (
            f"Genre strategy: {genre['top_genre']} is the "
            f"most represented genre ({genre['title_count']} "
            f"entries). Compare its catalog presence with "
            f"viewership before making further investments."
        ),

        (
            f"Content acquisition: In {trend['latest_year']}, "
            f"{trend['latest_count']} titles were added. "
            f"Use addition trends to support future catalog planning."
        ),

        (
            f"Movie format: Average movie duration is "
            f"{duration['average_duration']} minutes. "
            f"Study viewing completion and audience preferences "
            f"before changing content-length strategy."
        )
    ]

    return recommendations
