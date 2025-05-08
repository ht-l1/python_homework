import sqlite3
import os

os.makedirs('../db', exist_ok=True)
# All SQL statements should be executed within a try block, followed by a corresponing except block

# Task 1: Create a New SQLite Database
try:
    conn = sqlite3.connect("../db/magazines.db")
    print("Database created and connected successfully.")

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


    conn.close()
    print("Connection Closed.")
except Exception as e:
    print(f"Error: {e}")