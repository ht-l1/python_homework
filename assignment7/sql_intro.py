import sqlite3
import os

# Task 3: Populate Tables with Data
# Create functions, one for each of the tables, to add entries. Include code to handle exceptions as needed, and to ensure that there is no duplication of information. 
def add_publisher(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        print(f"Publisher '{name}' added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (name,))
        return cursor.fetchone()[0]
    except Exception as e:
        print(f"Error adding publisher '{name}': {e}")
        return None

def add_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", 
                      (name, publisher_id))
        print(f"Magazine '{name}' added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (name,))
        return cursor.fetchone()[0]
    except Exception as e:
        print(f"Error adding magazine '{name}': {e}")
        return None

def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", 
                      (name, address))
        print(f"Subscriber '{name}' added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' with address '{address}' already exists.")
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", 
                      (name, address))
        return cursor.fetchone()[0]
    except Exception as e:
        print(f"Error adding subscriber '{name}': {e}")
        return None

def add_subscription(conn, magazine_id, subscriber_id, expiration_date):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO subscriptions (magazine_id, subscriber_id, expiration_date) 
            VALUES (?, ?, ?)
        """, (magazine_id, subscriber_id, expiration_date))
        print(f"Subscription added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"This subscription already exists.")
        cursor.execute("""
            UPDATE subscriptions 
            SET expiration_date = ? 
            WHERE magazine_id = ? AND subscriber_id = ?
        """, (expiration_date, magazine_id, subscriber_id))
        print(f"Subscription expiration date updated.")
        return None
    except Exception as e:
        print(f"Error adding subscription: {e}")
        return None






# Task 1 and 2 below

os.makedirs('../db', exist_ok=True)
# All SQL statements should be executed within a try block, followed by a corresponding except block

# Task 1: Create a New SQLite Database
try:
    conn = sqlite3.connect("../db/magazines.db")
    print("Database created and connected successfully.")

    # This line tells SQLite to make sure the foreign keys are valid.
    conn.execute("PRAGMA foreign_keys = 1")

    # Task 2: Define Database Structure
    # create table: publishers
    try:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """)
        print("Publishers table created successfully.")
    except Exception as e:
        print(f"Error creating publishers table: {e}")

    # create table: magazines
    # There is a one-to-many relationship between publishers and magazines.
    try:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
        """)
        print("Magazines table created successfully.")
    except Exception as e:
        print(f"Error creating magazines table: {e}")

    # create table: subscribers > each subscriber has a name and an address
    try:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE(name, address)
        )
        """)
        print("Subscribers table created successfully.")
    except Exception as e:
        print(f"Error creating subscribers table: {e}")

    # create table: subscriptions 
    # > many-to-many association between subscribers and magazines
    # > stores the expiration_date (a string) for the subscription
    try:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            magazine_id INTEGER NOT NULL,
            subscriber_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id),
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            UNIQUE(magazine_id, subscriber_id)
        )
        """)
        print("Subscriptions table created successfully.")
    except Exception as e:
        print(f"Error creating subscriptions table: {e}")

    # commenting out the close statement as I cannot operate sample data on a closed database 
    # conn.close()
    # print("Connection Closed.")
except Exception as e:
    print(f"Error: {e}")


# Task 3: Add code to the main line of your program to populate each of the 4 tables with at least 3 entries. 
# Add publishers
publisher1_id = add_publisher(conn, "Beacon Hill Publishing")
publisher2_id = add_publisher(conn, "Atlantic Media Group")
publisher3_id = add_publisher(conn, "Seaboard Press")

# Add magazines
magazine1_id = add_magazine(conn, "Boston Review", publisher1_id)
magazine2_id = add_magazine(conn, "Cape & City Life", publisher1_id)
magazine3_id = add_magazine(conn, "Urban Atlantic", publisher2_id)
magazine4_id = add_magazine(conn, "The Ivy Quarterly", publisher2_id)
magazine5_id = add_magazine(conn, "Yankee Heritage", publisher3_id)

# Add subscribers
subscriber1_id = add_subscriber(conn, "Emily Donahue", "112 Charles St, Boston, MA 02114")
subscriber2_id = add_subscriber(conn, "Marcus Whitman", "112 Charles St, Boston, MA 02114")
subscriber3_id = add_subscriber(conn, "Tyler Cavanaugh", "88 Hope St, Providence, RI 02906")
subscriber4_id = add_subscriber(conn, "Aisha Brooks", "450 Beacon St, Boston, MA 02215")

# Add subscriptions
add_subscription(conn, magazine1_id, subscriber1_id, "2024-08-15")
add_subscription(conn, magazine2_id, subscriber1_id, "2024-09-12")
add_subscription(conn, magazine3_id, subscriber2_id, "2024-10-01")
add_subscription(conn, magazine1_id, subscriber3_id, "2025-01-20")
add_subscription(conn, magazine4_id, subscriber3_id, "2024-07-30")
add_subscription(conn, magazine5_id, subscriber4_id, "2024-10-10")

# Commit the changes
conn.commit()
print("Sample data added and committed successfully.")