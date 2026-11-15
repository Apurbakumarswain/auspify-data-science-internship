# Task 03 – Netflix Content Recommendation System

## Project Overview

This project implements a basic content-based recommendation system using Netflix titles and metadata. It recommends movies and TV shows based on similarities in their content features and categories.

## Objectives

- Extract relevant features from Netflix data.
- Perform text preprocessing.
- Convert textual data into numerical representations using TF-IDF.
- Calculate similarity using cosine similarity.
- Generate recommendations for selected Netflix titles.
- Evaluate recommendation relevance using category overlap.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- TF-IDF Vectorization
- Cosine Similarity

## Project Structure

```text
Task-03-Recommendation-System/
├── data/
├── notebooks/
│   └── recommendation_system.ipynb
├── outputs/
│   ├── recommendations.csv
│   └── similarity_results.csv
├── screenshots/
├── README.md
└── requirements.txt
```

## Methodology

### 1. Feature Extraction
Selected title, type, director, country, rating, and categories from the cleaned Netflix dataset.

### 2. Text Preprocessing
Converted text to lowercase, removed punctuation and special characters, and normalized extra spaces.

### 3. TF-IDF Vectorization
Used TF-IDF to convert text metadata into numerical feature vectors.

### 4. Similarity Calculation
Applied cosine similarity to measure similarity between Netflix titles.

### 5. Recommendation Generation
Created a recommendation function that returns the top five similar titles.

### 6. Recommendation Improvement
Developed a category-focused recommendation model using the `listed_in` feature to prioritize category similarity.

## Evaluation

Test title: Dick Johnson Is Dead

- Total recommendations: 5
- Category matches: 5
- Category match percentage: 100%

This evaluation measures category overlap rather than actual user satisfaction or recommendation accuracy.

## Output Files

- `recommendations.csv`: Contains recommended Netflix titles, categories, and similarity scores.
- `similarity_results.csv`: Contains the selected title, recommended titles, and similarity scores.

## Limitations

- The system uses metadata and categories rather than full descriptions.
- It does not use user ratings or viewing history.
- Titles sharing the same category can receive identical similarity scores.
- Category overlap is a simple relevance indicator, not a complete recommendation-quality metric.

## Conclusion

Successfully developed a basic content-based Netflix recommendation system using NLP fundamentals, TF-IDF vectorization, and cosine similarity. The project demonstrates feature extraction, text preprocessing, similarity analysis, recommendation generation, and basic evaluation.
