
import plotly.express as px


# --------------------------------------------------
# 1. CONTENT TYPE DISTRIBUTION
# --------------------------------------------------

def content_distribution_chart(data):

    fig = px.pie(
        data,
        names="Content Type",
        values="Count",
        title="Movie vs TV Show Distribution",
        hole=0.45
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return fig


# --------------------------------------------------
# 2. YEARLY CONTENT ADDITIONS
# --------------------------------------------------

def yearly_additions_chart(data):

    fig = px.line(
        data,
        x="date_added_year",
        y="Total Titles",
        color="type",
        markers=True,
        title="Netflix Content Additions Over Time",
        labels={
            "date_added_year": "Year",
            "Total Titles": "Number of Titles",
            "type": "Content Type"
        }
    )

    return fig


# --------------------------------------------------
# 3. TOP COUNTRIES
# --------------------------------------------------

def country_distribution_chart(data):

    fig = px.bar(
        data.sort_values("Total Titles"),
        x="Total Titles",
        y="country",
        orientation="h",
        title="Top Countries by Netflix Titles",
        labels={
            "country": "Country",
            "Total Titles": "Number of Titles"
        },
        text="Total Titles"
    )

    return fig


# --------------------------------------------------
# 4. TOP GENRES
# --------------------------------------------------

def genre_distribution_chart(data):

    fig = px.bar(
        data.sort_values("Total Titles"),
        x="Total Titles",
        y="genre",
        orientation="h",
        title="Most Popular Netflix Genres",
        labels={
            "genre": "Genre",
            "Total Titles": "Number of Titles"
        }
    )

    return fig


# --------------------------------------------------
# 5. CONTENT RATINGS
# --------------------------------------------------

def rating_distribution_chart(data):

    fig = px.bar(
        data,
        x="Content Rating",
        y="Total Titles",
        title="Netflix Content Rating Distribution",
        labels={
            "Content Rating": "Rating",
            "Total Titles": "Number of Titles"
        }
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    return fig


# --------------------------------------------------
# 6. RELEASE YEAR TRENDS
# --------------------------------------------------

def release_year_chart(data):

    fig = px.line(
        data,
        x="release_year",
        y="Total Titles",
        color="type",
        title="Netflix Titles by Original Release Year",
        markers=False,
        labels={
            "release_year": "Release Year",
            "Total Titles": "Number of Titles",
            "type": "Content Type"
        }
    )

    return fig


# --------------------------------------------------
# 7. MOVIE DURATION DISTRIBUTION
# --------------------------------------------------

def movie_duration_chart(df):

    movies = df[df["type"] == "Movie"].copy()

    fig = px.histogram(
        movies,
        x="duration_value",
        nbins=30,
        title="Distribution of Movie Durations",
        labels={
            "duration_value": "Duration (Minutes)"
        }
    )

    return fig
