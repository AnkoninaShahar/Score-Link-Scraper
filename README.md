# Basketball Statistics Link Scraper
**AUTHOR . . . . . . .** Shahar Ankonina                                                                         
**DESCRIPTION. . .** Automated web scraper for extracting game and player data links from basketball statistics websites

---
## About
This project is designed to automate the data collection process from basketball statistics platforms. It systematically navigates through league schedules and player directories to extract direct URLs, which can then be used for deep-data harvesting, scouting reports, or machine learning datasets.

---
## Features
- *Automated Navigation:* Efficiently crawls through multi-page directories to find specific game.
- *Customizable Filters:* Allows users to target specific years for more refined data extraction.
- *Data Export:* Seamlessly compiles gathered links into structured formats for easy integration into secondary scraping scripts.
- *Error Handling:* Includes robust exception handling to manage site timeouts or structural changes in the target website.
- *Headless Execution:* Optimized to run in the background without requiring a visual browser window.

---
## Tech Stack
- *Programming Languages:* Python
- *Libraries & Frameworks:* BeautifulSoup4, Selenium, Requests
- *Tools & Platforms:* Git/GitHub, VS Code, WebDriver

---
## Installation
Follow these steps to run the project locally:

```bash
# Clone the repo
git clone [https://github.com/AnkoninaShahar/Link-Scraper.git](https://github.com/AnkoninaShahar/Link-Scraper.git)

# Navigate into the directory
cd Link-Scraper

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py

```

---
## Usage
- Before running, ensure you have the appropriate WebDriver (e.g., ChromeDriver) installed and added to your system path.
- **Run with specific year: (default = 2025)**
  ```bash
  python main.py --year=2025
  
  ```
- **Output:** Saves links in a folder for a given year in individual text files for each month
