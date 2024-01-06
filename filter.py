import pandas as pd

# Read ratings.csv and movies.csv into DataFrames
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# Step 1: Group user ratings based on movieId and apply aggregation operations
ratings_grouped = ratings.groupby('movieId').agg({'rating': ['count', 'mean']}).reset_index()

# Step 2: Inner join on dataframe created from movies.csv and the grouped df from step 1
merged_data = pd.merge(movies, ratings_grouped, on='movieId', how='inner')

# Step 3: Filter only those movies which have more than 50 user ratings
filtered_movies = merged_data[merged_data['rating']['count'] > 50]

# Display the filtered movies DataFrame
print(filtered_movies.head())
