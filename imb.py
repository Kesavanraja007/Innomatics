import pandas as pd
import random  # Add this import

# Read links.csv into DataFrame
links = pd.read_csv('links.csv')

# Assuming you have a function to fetch IMDB ratings by IMDB id
def get_imdb_rating(imdb_id):
    # Implement your logic to fetch the IMDB rating for the given imdb_id
    # This might involve web scraping or using an API

    # Placeholder: Return a random value
    return round(random.uniform(7.0, 9.0), 1)

# Fetch IMDB ratings for each movie
links['imdb_rating'] = links['imdbId'].apply(get_imdb_rating)

# Identify the movie with the highest IMDB rating
highest_rated_movie = links.loc[links['imdb_rating'].idxmax(), 'movieId']

# Print the result
print(f"The movieId of the movie with the highest IMDB rating is: {highest_rated_movie}")
