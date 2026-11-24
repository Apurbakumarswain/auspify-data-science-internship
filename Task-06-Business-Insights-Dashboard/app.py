
import streamlit as st
import pandas as pd

from src.analysis import (
    load_data,
    get_kpi_metrics,
    get_content_distribution,
    get_yearly_additions,
    get_country_distribution,
    get_genre_distribution,
    get_rating_distribution,
    get_release_year_trends
)

from src.visualizations import (
    content_distribution_chart,
    yearly_additions_chart,
    country_distribution_chart,
    genre_distribution_chart,
    rating_distribution_chart,
    release_year_chart,
    movie_duration_chart
)

from src.model import train_classification_model

from src.business_insights import generate_recommendations


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Netflix Business Insights",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_dashboard_data():
    return load_data()


df = load_dashboard_data()


# --------------------------------------------------
# 3. HEADER
# --------------------------------------------------

st.title("📊 Netflix Business Insights Dashboard")

st.markdown(
    """
    Explore Netflix's content catalog through data analytics,
    machine learning and business insights.
    """
)

st.divider()


# --------------------------------------------------
# 4. SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

content_types = st.sidebar.multiselect(
    "Select Content Type",
    options=sorted(df["type"].unique()),
    default=sorted(df["type"].unique())
)

year_range = st.sidebar.slider(
    "Select Release Year Range",
    min_value=int(df["release_year"].min()),
    max_value=int(df["release_year"].max()),
    value=(
        int(df["release_year"].min()),
        int(df["release_year"].max())
    )
)

filtered_df = df[
    (df["type"].isin(content_types))
    &
    (df["release_year"].between(
        year_range[0],
        year_range[1]
    ))
]


# --------------------------------------------------
# 5. EXECUTIVE OVERVIEW
# --------------------------------------------------

st.header("Executive Overview")

metrics = get_kpi_metrics(filtered_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Titles",
    f"{metrics['total_titles']:,}"
)

col2.metric(
    "Movies",
    f"{metrics['total_movies']:,}"
)

col3.metric(
    "TV Shows",
    f"{metrics['total_tv_shows']:,}"
)

col4.metric(
    "Countries",
    f"{metrics['total_countries']:,}"
)

st.caption(
    "KPIs reflect the selected filters. Country counts represent "
    "distinct country names associated with filtered titles."
)

st.divider()


# --------------------------------------------------
# 6. CONTENT DISTRIBUTION
# --------------------------------------------------

st.header("Content Distribution")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        content_distribution_chart(
            get_content_distribution(filtered_df)
        ),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        yearly_additions_chart(
            get_yearly_additions(filtered_df)
        ),
        use_container_width=True
    )


# --------------------------------------------------
# 7. GEOGRAPHIC AND GENRE ANALYSIS
# --------------------------------------------------

st.header("Geographic and Genre Analysis")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        country_distribution_chart(
            get_country_distribution(filtered_df)
        ),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        genre_distribution_chart(
            get_genre_distribution(filtered_df)
        ),
        use_container_width=True
    )


# --------------------------------------------------
# 8. CONTENT RATING ANALYSIS
# --------------------------------------------------

st.header("Content Rating Analysis")

st.plotly_chart(
    rating_distribution_chart(
        get_rating_distribution(filtered_df)
    ),
    use_container_width=True
)


# --------------------------------------------------
# 9. RELEASE YEAR ANALYSIS
# --------------------------------------------------

st.header("Content Release Trends")

st.plotly_chart(
    release_year_chart(
        get_release_year_trends(filtered_df)
    ),
    use_container_width=True
)


# --------------------------------------------------
# 10. MOVIE DURATION ANALYSIS
# --------------------------------------------------

st.header("Movie Duration Analysis")

st.plotly_chart(
    movie_duration_chart(filtered_df),
    use_container_width=True
)


# --------------------------------------------------
# 11. MACHINE LEARNING
# --------------------------------------------------

st.divider()

st.header("Machine Learning Prediction")

st.write(
    "Logistic Regression classifies Netflix titles "
    "as Movies or TV Shows using selected catalog features."
)

if st.button("Run Model Evaluation"):

    with st.spinner("Training and evaluating model..."):

        result = train_classification_model(df)

    st.success("Model evaluation completed!")

    st.metric(
        "Model Accuracy",
        f"{result['accuracy'] * 100:.2f}%"
    )

    report_df = pd.DataFrame(
        result["report"]
    ).transpose()

    st.subheader("Classification Report")

    st.dataframe(
        report_df,
        use_container_width=True
    )

    matrix_df = pd.DataFrame(
        result["confusion_matrix"],
        index=result["classes"],
        columns=result["classes"]
    )

    st.subheader("Confusion Matrix")

    st.dataframe(
        matrix_df,
        use_container_width=True
    )


# --------------------------------------------------
# 12. BUSINESS RECOMMENDATIONS
# --------------------------------------------------

st.divider()

st.header("Business Insights and Recommendations")

recommendations = generate_recommendations(df)

for i, recommendation in enumerate(
    recommendations,
    start=1
):

    st.info(f"{i}. {recommendation}")


# --------------------------------------------------
# 13. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Netflix Business Insights Dashboard | "
    "Data Science Internship Task 6"
)
