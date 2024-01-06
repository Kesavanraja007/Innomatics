import pandas as pd

# Assuming you have a DataFrame named tags_data with columns 'movieId' and 'tag'
# Replace 'your_tags_data.csv' with the actual path to your tags dataset
tags_file_path = 'tags.csv'
tags_data = pd.read_csv(tags_file_path)

# Replace 'Matrix, The (1999)' with the exact movie name you are looking for
movie_name = 'Matrix, The (1999)'

# Filter tags for the specified movie
movie_tags = tags_data.loc[tags_data['movieId'] == movie_name, 'tag'].tolist()

# Print the result
print(f"The tags for '{movie_name}' submitted by users are: {movie_tags}")
