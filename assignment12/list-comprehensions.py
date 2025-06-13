import pandas as pd

# Task 3 - List Comprehensions
# Add code that reads the contents of ../csv/employees.csv into a DataFrame.
df = pd.read_csv("../csv/employees.csv")

# Using a list comprehension, create a list of the employee names, first_name + space + last_name. 
# The list comprehension should iterate through the rows of the DataFrame. df.iterrows() gives an iterable list of rows. Each row is a tuple, where the first element of the tuple is the index, and the second element is a dict with the key/value pairs from the row.
full_names = [f"{row['first_name']} {row['last_name']}" for index, row in df.iterrows()]
# Print the resulting list. 
print("Employee names:")
print(full_names)

# Using a list comprehension, create another list from the previous list of names. This list should include only those names that contain the letter "e". Print this list.
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames only containing the letter 'e':")
print(names_with_e)