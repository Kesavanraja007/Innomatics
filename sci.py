import pandas as pd

# Read ratings.csv and movies.csv into DataFrames
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# Step 1: Group user ratings based on movieId and apply aggregation operations
ratings_grouped = ratings.groupby('movieId')['rating'].agg(['count', 'mean']).reset_index()

# Step 2: Inner join on dataframe created from movies.csv and the grouped df from step 1
merged_data = pd.merge(movies, ratings_grouped, on='movieId', how='inner')

# Step 3: Filter only those movies which have more than 50 user ratings
filtered_movies = merged_data[merged_data['count'] > 50]

# Filter Sci-Fi movies
sci_fi_movies = filtered_movies[filtered_movies['genres'].str.contains('Sci-Fi')]

# Sort Sci-Fi movies based on the count of ratings in descending order
sorted_sci_fi_movies = sci_fi_movies.sort_values(by='count', ascending=False)

# Get the title of the third most popular Sci-Fi movie
third_most_popular_sci_fi_movie = sorted_sci_fi_movies.iloc[2]['title']

# Print the result
print(f"The third most popular Sci-Fi movie based on the number of user ratings is: {third_most_popular_sci_fi_movie}")
