import pandas as pd

# Replace 'ratings.csv' with the actual path to your ratings CSV file
file_path = 'ratings.csv'

# Read the CSV file into a DataFrame
ratings_data = pd.read_csv(file_path)

# Get the number of unique userId values
unique_user_ids_count = ratings_data['userId'].nunique()

# Print the result
print(f"The number of unique userId values in 'ratings.csv' is: {unique_user_ids_count}")
