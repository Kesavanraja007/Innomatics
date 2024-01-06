import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named ratings_data with columns 'movieId' and 'rating'
# Replace 'your_ratings_data.csv' with the actual path to your ratings dataset
ratings_file_path = 'ratings.csv'
ratings_data = pd.read_csv(ratings_file_path)

# Assuming you have a DataFrame named movies_data with columns 'movieId' and 'title'
# Replace 'your_movies_data.csv' with the actual path to your movies dataset
movies_file_path = 'movies.csv'
movies_data = pd.read_csv(movies_file_path)

# Replace 'Fight Club (1999)' with the exact movie name you are looking for
movie_name = 'Fight Club (1999)'

# Get the movieId for the specified movie
movie_id = movies_data.loc[movies_data['title'] == movie_name, 'movieId'].values[0]

# Filter ratings for the specified movie
movie_ratings = ratings_data.loc[ratings_data['movieId'] == movie_id, 'rating']

# Plot a histogram
plt.figure(figsize=(10, 6))
plt.hist(movie_ratings, bins=10, edgecolor='black', alpha=0.7)
plt.title(f'Distribution of User Ratings for "{movie_name}"')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
