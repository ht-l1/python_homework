import pandas as pd

# Task 5 - Extending DataFrame
# Create a class called DFPlus. It should inherit from the Pandas DataFrame class. You are going to add a single method to the class. You do not need an __init__ method, because you are going to use the one already provided.
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    # declare a function called print_with_headers(). It only takes one argument, self. 
    def print_with_headers(self):
        # You need to know the length of the DataFrame. len(self).  
        total_rows = len(self)
        
        # When you print a big DataFrame, you can't see the column headers because they scroll up. This function will provide a way to print the DataFrame giving column headers every 10 lines. The function will print the whole DataFrame in a loop, printing 10 rows at a time.
        for start_row in range(0, total_rows, 10):
            end_row = min(start_row + 10, total_rows)
            
            # how do you get a given 10 rows? You have access to super().iloc so you can specify the ten line slice you want. And then you just print what you get back, looping until you get to the bottom.
            print(super().iloc[start_row:end_row])
            print()  # Add a blank line between chunks

# Main function
if __name__ == "__main__":
    # Using the from_csv() class method, create a DFPlus instance from "../csv/products.csv".
    dfp = DFPlus.from_csv("../csv/products.csv")
    # Use the print_with_headers() method of your DFPlus instance to print the DataFrame.
    dfp.print_with_headers()