from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Remove this if you want to see the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Target URL
url = 'https://www.bdjobs.com/jobsearch.asp'
driver.get(url)

# Wait for the page to load completely
time.sleep(5)  # Use WebDriverWait in production

# Lists to store scraped data
jobs = []

# Find job cards
job_cards = driver.find_elements(By.CSS_SELECTOR, '.row.job-card')

for card in job_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, '.card-title-text a').text
        link = card.find_element(By.CSS_SELECTOR, '.card-title-text a').get_attribute('href')
        company = card.find_element(By.CSS_SELECTOR, '.card-company-text').text
        location = card.find_element(By.CSS_SELECTOR, '.card-location-text').text
        deadline = card.find_element(By.CSS_SELECTOR, '.card-deadline-text').text

        jobs.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'Deadline': deadline,
            'Link': link
        })
    except:
        continue

# Close the browser
driver.quit()

# Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("bdjobs_selenium.csv", index=False)
print(f"Scraped {len(df)} jobs and saved to 'bdjobs_selenium.csv'")