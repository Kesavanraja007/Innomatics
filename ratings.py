import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'ratings.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Extract unique user IDs
unique_user_ids = data['userid'].unique()

# Print the unique user IDs
print("Unique User IDs:")
for user_id in unique_user_ids:
    print(user_id)
