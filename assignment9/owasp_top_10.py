# Use your browser developer tools to view this page: [https://owasp.org/www-project-top-ten/].  
# You are going to extract the top 10 security risks reported there.  Figure out how you will find them.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

time.sleep(5)

results = []

try:
    # Find each of the top 10 vulnerabilities.  Hint: You will need XPath.  
    vulnerabilities = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Top 10 Web Application Security Risks')]/following-sibling::ul[1]/li")
    
    # For each of the top 10 vulnerabilites, keep the vulnerability title and the href link in a dict.  
    for vuln in vulnerabilities:
        if 'A' in vuln.text and any(digit in vuln.text for digit in "0123456789"):
            title = vuln.text
            link = vuln.get_attribute('href')
            
            # Accumulate these dict objects in a list.
            vuln_info = {
                "Title": title,
                "Link": link
            }
            
            results.append(vuln_info)
    
except Exception as e:
    print(f"Error extracting vulnerabilities: {e}")

# Print out the list to make sure you have the right data.  
print("\nOWASP Top 10 Vulnerabilities:")
for i, vuln in enumerate(results, 1):
    print(f"{i}. {vuln['Title']} - {vuln['Link']}")

df = pd.DataFrame(results)

df.to_csv("owasp_top_10.csv", index=False)
print("\nData written to owasp_top_10.csv")

driver.quit()