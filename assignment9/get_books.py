# Task 3: Write a Program to Extract this Data
# Task 4: Write out the Data

# The program should import from selenium and webdriver_manager, as shown in your lesson.  You also need pandas and json.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Add code to load the web page given in task 2.
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

# You need to make sure your program pauses between pages.  Fast screen scraping, where many requests are sent in short order, is an abuse of the privilege.
time.sleep(5)

# Find all the li elements in that page for the search list results.  You use the class values you stored in task 2 step 3.  Also use the tag name when you do the find, to make sure you get the right elements.
search_results = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
print(f"Found {len(search_results)} search results")

# Within your program, create an empty list called results.  You are going to add dict values to this list, one for each search result.
results = []

# Main loop: You iterate through the list of li entries.   
for result in search_results:
    try:
        # For each, you find the entry that contains title of the book, and get the text for that entry. 
        title_element = result.find_element(By.CSS_SELECTOR, "h2.cp-title")
        title = title_element.text
        
        # Then you find the entries that contain the authors of the book, and get the text for each. If you find more than one author, you want to join the author names with a semicolon ; between each.
        author_elements = result.find_elements(By.CSS_SELECTOR, "span.cp-author-link")
        authors = [author.text for author in author_elements]
        author_text = "; ".join(authors) if authors else "Unknown"
        
        # Then you find the div that contains the format and the year, and then you find the span entry within it that contains this information.  You get that text too.
        format_year_div = result.find_element(By.CSS_SELECTOR, "div.cp-format-info")
        format_year_span = format_year_div.find_element(By.CSS_SELECTOR, "span.display-info-primary")
        format_year = format_year_span.text
        
        # You now have three pieces of text.  Create a dict that stores these values, with the keys being Title, Author, and Format-Year.  Then append that dict to your results list.
        book_info = {
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        }
        
        # Add to results list
        results.append(book_info)
        
    except Exception as e:
        print(f"Error processing a search result: {e}")

# Create a DataFrame from this list of dicts.  Print the DataFrame.
df = pd.DataFrame(results)
print("\nDataFrame of search results:")
print(df)

# Write the DataFrame to a file called get_books.csv, within the assignment9 folder.  Examine the file to see if it looks right.
df.to_csv("get_books.csv", index=False)
print("\nData written to get_books.csv")

# Write the results list out to a file called get_books.json, also within the assignment9 folder.  You should write it out in JSON format.  Examine the file to see if it looks right.
with open("get_books.json", "w") as f:
    json.dump(results, f, indent=4)
print("Data written to get_books.json")

# Close the browser
driver.quit()