# Task 5: Read Data into a DataFrame
# You will now use Pandas to create summary data from the ../db/lesson.db database you populated as part of the lesson.  
# We want to find out how many times each product has been ordered, and what was the total price paid by product.

import pandas as pd
import sqlite3

try:
    conn = sqlite3.connect('../db/lesson.db')
    print("Successfully connected to the lesson.db database.")
    
    #  The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price from a JOIN of the line_items table and the product table. Hint: Your ON statement would be ON line_items.product_id = products.product_id.
    query = """
    SELECT line_items.line_item_id, line_items.quantity, 
           products.product_id, products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """
    
    # Read data into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Print the first 5 lines of the resulting DataFrame. 
    print("\nFirst 5 rows of the original DataFrame:")
    print(df.head())
    
    # Add a column to the DataFrame called "total". This is the quantity times the price. (This is easy: df['total'] = df['quantity'] * df['price'].) 
    df['total'] = df['quantity'] * df['price']
    
    # Print out the first 5 lines of the DataFrame to make sure this works.
    print("\nFirst 5 rows with total column:")
    print(df.head())
    
    # Add groupby() code to group by the product_id. Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'. 
    summary_df = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    })
    
    # Print out the first 5 lines of the resulting DataFrame. Run the program to see if it is correct so far.
    print("\nFirst 5 rows of the summary DataFrame:")
    print(summary_df.head())
    
    # Sort the DataFrame by the product_name column.
    summary_df = summary_df.sort_values('product_name')
    
    print("\nSorted summary DataFrame:")
    print(summary_df.head())
    
    # Add code to write this DataFrame to a file order_summary.csv, which should be written in the assignment7 directory. Verify that this file is correct.
    summary_df.to_csv('order_summary.csv')
    print("\nSummary data written to order_summary.csv")
    
    conn.close()
    print("\nConnection closed.")
except Exception as e:
    print(f"Error: {e}")