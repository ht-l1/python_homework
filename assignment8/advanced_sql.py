import sqlite3

def main():
    conn = sqlite3.connect('../db/lesson.db')
    conn.row_factory = sqlite3.Row
    
    # Task 1: Complex JOINs with Aggregation
    print("\n--- Task 1: Complex JOINs with Aggregation ---")
    # Find the total price of each of the first 5 orders.  There are several steps.  You need to join the orders table with the line_items table and the products table.  You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of the product price times the line_item quantity.  Then, you ORDER BY order_id and LIMIT 5.  You don't need a subquery. Print out the order_id and the total price for each of the rows returned.
    task1_query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5
    """
    
    cursor = conn.execute(task1_query)
    for row in cursor:
        print(f"Order ID: {row['order_id']}, Total Price: ${row['total_price']:.2f}")
    
    # Task 2: Understanding Subqueries
    print("\n--- Task 2: Understanding Subqueries ---")
    # For each customer, find the average price of their orders.  This can be done with a subquery. You compute the price of each order as in part 1, but you return the customer_id and the total_price.  That's the subquery. You need to return the total price using AS total_price, and you need to return the customer_id with AS customer_id_b, for reasons that will be clear in a moment.  In your main statement, you left join the customer table with the results of the subquery, using ON customer_id = customer_id_b.  You aliased the customer_id column in the subquery so that the column names wouldn't collide.  Then group by customer_id -- this GROUP BY comes after the subquery -- and get the average of the total price of the customer orders.  Return the customer name and the average_total_price.
    task2_query = """
    SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) AS order_totals ON c.customer_id = order_totals.customer_id_b
    GROUP BY c.customer_id
    """
    
    cursor = conn.execute(task2_query)
    for row in cursor:
        avg_price = row['average_total_price']
        if avg_price is None:
            print(f"Customer: {row['customer_name']}, Average Order Total: No orders")
        else:
            print(f"Customer: {row['customer_name']}, Average Order Total: ${avg_price:.2f}")
      
    # Task 3: An Insert Transaction Based on Data
    print("\n--- Task 3: An Insert Transaction Based on Data ---")
    # You want to make sure that the foreign keys in the INSERT statements are valid.  So, add this line to your script, right after the database connection:
    conn.execute("PRAGMA foreign_keys = 1")
    conn.execute("BEGIN TRANSACTION")
    
    try:
        # Customer named Perez and Sons
        # You first need to do a SELECT statement to retrieve the customer_id
        customer_query = "SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'"
        customer_cursor = conn.execute(customer_query)
        customer_row = customer_cursor.fetchone()
        if customer_row is None:
            raise Exception("Customer 'Perez and Sons' not found in the database")
        customer_id = customer_row['customer_id']
        
        # The employee creating the order is Miranda Harris
        # another to retrieve the employee_id
        employee_query = "SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'"
        employee_cursor = conn.execute(employee_query)
        employee_row = employee_cursor.fetchone()
        if employee_row is None:
            raise Exception("Employee 'Miranda Harris' not found in the database")
        employee_id = employee_row['employee_id']
        
        # The customer wants 10 of each of the 5 least expensive products
        # another to retrieve the product_ids of the 5 least expensive products
        products_query = """
        SELECT product_id, product_name, price 
        FROM products 
        ORDER BY price ASC 
        LIMIT 5
        """
        product_cursor = conn.execute(products_query)
        product_ids = [row['product_id'] for row in product_cursor]
        
        # create the order record and the 5 line_item records comprising the order.  
        # use the customer_id, employee_id, and product_id values you obtained from the SELECT statements
        # you need the order_id for the order record you insert to be able to insert line_item records for that order.  You can have this value returned by adding the following clause to the INSERT statement for the order: RETURNING order_id
        order_insert = """
        INSERT INTO orders (customer_id, employee_id, date) 
        VALUES (?, ?, DATE('now')) 
        RETURNING order_id
        """
        order_cursor = conn.execute(order_insert, (customer_id, employee_id))
        order_id = order_cursor.fetchone()[0]
        
        # use the order_id for the order record you created in the line_items records
        for product_id in product_ids:
            line_item_insert = """
            INSERT INTO line_items (order_id, product_id, quantity) 
            VALUES (?, ?, 10)
            """
            conn.execute(line_item_insert, (order_id, product_id))
        
        # Commit the transaction
        conn.commit()
        
        # using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each
        result_query = """
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
        """
        result_cursor = conn.execute(result_query, (order_id,))
        
        print(f"Created order {order_id} with the following items:")
        for row in result_cursor:
            print(f"Line Item ID: {row['line_item_id']}, Quantity: {row['quantity']}, Product: {row['product_name']}")
        
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {e}")
    
    # Task 4: Aggregation with HAVING
    print("\n--- Task 4: Aggregation with HAVING ---")
    task4_query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5
    """
    
    cursor = conn.execute(task4_query)
    for row in cursor:
        print(f"Employee ID: {row['employee_id']}, Name: {row['first_name']} {row['last_name']}, Order Count: {row['order_count']}")
    
    conn.close()

if __name__ == "__main__":
    main()