# Netflix Dataset – Exploratory Data Analysis Report

## 1. Project Overview

This project performs Exploratory Data Analysis (EDA) on a Netflix titles dataset to identify patterns, trends, and insights related to content distribution, countries, genres, release years, ratings, and content additions.

The objective is to understand the characteristics of Netflix's content catalogue through statistical analysis and data visualization.

## 2. Dataset Information

- **Dataset:** Netflix Titles Dataset
- **Total Records:** 8,790
- **Total Features:** 15
- **Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook in VS Code

The cleaned dataset generated during Task 1 was used for this analysis.

## 3. Data Quality Verification

The dataset was checked for missing values and duplicate records.

| Check | Result |
|---|---:|
| Total Rows | 8,790 |
| Total Columns | 15 |
| Missing Values | 0 |
| Duplicate Rows | 0 |

The dataset passed all final data-quality checks.

## 4. Key Findings

### 4.1 Content Distribution

- Movies: 6,126 (69.69%)
- TV Shows: 2,664 (30.31%)

Movies represent the majority of titles in the dataset.

### 4.2 Top 10 Countries

| Country | Title Associations |
|---|---:|
| United States | 3,240 |
| India | 1,057 |
| United Kingdom | 638 |
| Pakistan | 421 |
| Canada | 271 |
| Japan | 259 |
| South Korea | 214 |
| France | 213 |
| Spain | 182 |
| Mexico | 138 |

The United States has the highest number of country-title associations, followed by India and the United Kingdom.

*Note: A title can be associated with multiple countries, so these figures are not mutually exclusive.*

### 4.3 Top 10 Content Categories

| Category | Title Associations |
|---|---:|
| International Movies | 2,752 |
| Dramas | 2,426 |
| Comedies | 1,674 |
| International TV Shows | 1,349 |
| Documentaries | 869 |
| Action & Adventure | 859 |
| TV Dramas | 762 |
| Independent Movies | 756 |
| Children & Family Movies | 641 |
| Romantic Movies | 616 |

International Movies and Dramas are the most frequently represented categories.

*Note: A title may belong to multiple categories.*

### 4.4 Content Addition Trends

The number of titles added to Netflix increased substantially after 2016.

- 2019 recorded the highest number of additions: 2,016.
- 2020 recorded 1,879 additions.
- 2021 recorded 1,498 additions through September 25.

The 2021 figure represents a partial year and should not be directly compared with complete years.

### 4.5 Movie and TV Show Duration

- Average movie duration: 99.58 minutes.
- Average TV show duration: 1.75 seasons.

Movies and TV shows were analyzed separately because their duration measurements use different units.

### 4.6 Release Year Analysis

- Oldest release year: 1925.
- Latest release year: 2021.
- Average release year: approximately 2014.18.
- 2018 had the highest number of titles, with 1,146.

The dataset contains a strong concentration of titles released between 2016 and 2020.

### 4.7 Content Rating Distribution

| Rating | Titles |
|---|---:|
| TV-MA | 3,205 |
| TV-14 | 2,157 |
| TV-PG | 861 |
| R | 799 |
| PG-13 | 490 |
| TV-Y7 | 333 |
| TV-Y | 306 |
| PG | 287 |
| TV-G | 220 |
| NR | 79 |
| G | 41 |
| TV-Y7-FV | 6 |
| NC-17 | 3 |
| UR | 3 |

TV-MA is the most common content rating, followed by TV-14.

### 4.8 Monthly Content Additions

- July: 827 titles.
- December: 812 titles.
- September: 769 titles.
- February: 562 titles.

July had the highest number of content additions, while February had the lowest.

## 5. Visualizations

The following charts were generated and saved in the `visualizations` folder:

1. Content distribution by type
2. Top 10 countries
3. Top 10 content categories
4. Yearly content addition trends
5. Average movie and TV show duration
6. Content distribution by release year
7. Content rating distribution
8. Monthly content additions

## 6. Conclusion

The exploratory analysis reveals that Netflix's catalogue in this dataset contains a larger proportion of movies than TV shows. The United States and India have substantial country-title representation, while International Movies and Dramas are prominent categories.

Content additions increased considerably after 2016 and reached their highest recorded level in 2019. The analysis also highlights that July had the most content additions among the months.

Overall, EDA helped identify meaningful patterns and provided a clearer understanding of the Netflix dataset through statistical summaries and visualizations.

## 7. Limitations

- Titles can be associated with multiple countries and categories.
- The dataset reflects a particular snapshot and does not necessarily represent Netflix's current catalogue.
- The 2021 content-addition data covers only part of the year.
- Correlation or association in this dataset does not establish causation.

## 8. Skills Demonstrated

- Exploratory Data Analysis
- Data inspection and statistical analysis
- Pandas data manipulation
- Matplotlib and Seaborn visualization
- Data interpretation
- Technical reporting
