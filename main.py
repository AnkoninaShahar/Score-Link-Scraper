from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--year", type=int, default=2025)
year = parser.parse_args().year

folder_name = f"statistics_links_{year}"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Path to chromedriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

for i in range(12):
    print(f"{months[i]}... Scraping...")

    # Navigate to the month schedule page
    url = f"https://www.basketball-reference.com/leagues/NBA_{year if i < 9 else year + 1}_games-{months[i]}.html"
    driver.get(url)

    # Wait up to 10 seconds for the table to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "schedule"))
        )
    except Exception as e:
        print(f"No games in {months[i]}")
        continue

    # Find all <a> elements on the page
    all_links = driver.find_elements(By.TAG_NAME, "a")

    # Filter only boxscore links
    boxscore_links = []
    key_word = "/boxscores/"
    for link in all_links:
        href = link.get_attribute("href")
        if href and key_word in href:
            index = href.find(key_word) + len(key_word)
            pbp = href[0:index] + "pbp/" + href[index:]
            boxscore_links.append(pbp)

    # Remove duplicates
    boxscore_links = list(set(boxscore_links))

    filtered_links = [url for url in boxscore_links if ".html" in url]
    with open(f"statistics_links_{year}\\boxscores_{months[i]}.txt", "w") as f:
        for url in filtered_links:
            f.write(url + "\n")
    
    print(f"{months[i]}... Done!")

print("Scraping Complete!")
driver.quit()
