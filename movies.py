import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'ratings.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Get the shape of the DataFrame
rows, columns = data.shape

# Print the results
print(f"The CSV file has {rows} rows and {columns} columns.")
