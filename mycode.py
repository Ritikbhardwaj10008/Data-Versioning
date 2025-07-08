import pandas as pd
import os

# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

new_row_loc3 = {'Name': 'GF3', 'Age': 21, 'City': 'City3'}
df.loc[len(df.index)] = new_row_loc3

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)  # exists ok means agar folder already hia to vo dubara nhi bnaega


# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')  # root level pr directory and file name 

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)   # to save the csv file

print(f"CSV file saved to {file_path}")



# this will create a csv(named data) file in which my data is present 