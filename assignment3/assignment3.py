import pandas as pd
import numpy as np
import json
from datetime import datetime

# --------------------------------------------
# Task 1: Creating and Manipulating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("1.1 Create a DataFrame from a dictionary:", "\n", task1_data_frame, "\n")

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("1.2 Add a new column:", "\n", task1_with_salary, "\n")

task1_older =  task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("1.3 Modify an existing column:", "\n", task1_older, "\n")

task1_older.to_csv('employees.csv', index=False)
print("1.4 Save the DataFrame as a CSV file:")
with open('employees.csv', 'r') as f:
    print(f.read())

# --------------------------------------------
# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv')
print("2.1. Read data from a CSV file:", "\n", task2_employees, "\n")

# 2.2 Read data from a JSON file:
additional_employees = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]
}

with open('additional_employees.json', 'w') as f:
    json.dump(additional_employees, f)

json_employees = pd.read_json('additional_employees.json')
print("2.2 Read data from a JSON file:", "\n", json_employees, '\n')
# End of 2.2

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("2.3. Combine DataFrames:", "\n", more_employees)

# --------------------------------------------
# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = more_employees.head(3)
print("3.1 Use the head() method:", "\n", first_three, "\n")

last_two = more_employees.tail(2)
print("3.2 Use the tail() method:", "\n", last_two, "\n")

employee_shape = more_employees.shape
print("3.3 Get the shape of a DataFrame", "\n", employee_shape, "\n")

print("3.4 Use the info() method:", "\n", more_employees.info(), "\n")

# --------------------------------------------
# Task 4: Data Cleaning
dirty_data = """Name, Age, City, Department, Salary, Hire Date
James O'Connor, 42, Boston, IT, 92000, 2015-09-10
Emily Rivera, N/A, Providence, HR, 68000, 2020-02-18
Michael Thompson, 39, Portland, Finance, unknown, 2017-12-05
James O'Connor, 42, Boston, IT, 92000, 2015-09-10
Sophia Chen, 31, Hartford, Marketing, 70000, 2019/06/15
Brian Kennedy, unknown, Bangor, it, n/a, 2016-08-30
"""

with open('dirty_data.csv', 'w') as f:
    f.write(dirty_data)

# 4.1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv('dirty_data.csv',  skipinitialspace=True)
print("4.1__________:", "\n", dirty_data)

clean_data = dirty_data.copy()

# 4.2. Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print("4.2__________", "\n", clean_data)

# 4.3 Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("4.3__________", "\n", clean_data)

# 4.4 Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors = 'coerce')
print("4.4__________", "\n", clean_data)

# 4.5 Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("4.5__________:", "\n", clean_data)

# 4.6 Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format="mixed")
print("4.6__________", "\n", clean_data)

# 4.7 Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("4.7__________", "\n", clean_data)