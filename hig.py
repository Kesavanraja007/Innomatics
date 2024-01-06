import pandas as pd

# Read links.csv and ratings.csv into DataFrames
links = pd.read_csv('links.csv')
ratings = pd.read_csv('ratings.csv')

# Step 1: Group user ratings based on movieId and apply aggregation operations
ratings_grouped = ratings.groupby('movieId')['rating'].agg(['count', 'mean']).reset_index()

# Step 2: Inner join on dataframe created from links.csv and the grouped df from step 1
merged_data = pd.merge(links, ratings_grouped, on='movieId', how='inner')

# Step 3: Filter only those movies which have more than 50 user ratings
filtered_movies = merged_data[merged_data['count'] > 50]

# Identify the Sci-Fi movie with the highest average rating
highest_rated_sci_fi_movie = filtered_movies.loc[filtered_movies['mean'].idxmax(), 'movieId']

# Print the result
print(f"The movieId of the Sci-Fi movie with the highest average rating is: {highest_rated_sci_fi_movie}")
