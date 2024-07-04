### Projects from Udemy Course: Complete Web Scraping, Web Crawling and Web Automation Bootcamp using Python 3, Selenium, BeautifulSoup and Chromium

---

### Project 1: api_scraper

#### Description
This project scrapes job data from the RemoteOK API. The data is filtered and exported to an Excel file, and also sent via email.

#### Changes Made
Custom implementation based on the original course material.

#### Files
- `remoteok_scraper.py`: Main script for scraping and exporting.
- `remote_jobs.xlsx`: Output file generated with job data.

#### Usage
1. Install dependencies using `pip install requests pandas smtplib`.
2. Run `python remoteok_scraper.py` to fetch and save job data to an Excel file.
3. Verify email configuration in the script before sending data via email.

#### Notes
- Ensure you have appropriate permissions and configurations to send emails from your Gmail account.

---

### Project 2: html scraper

#### Description
This project scrapes product data from Mercado Libre URLs. The data is extracted and saved to a CSV file named based on the current date.

#### Changes Made
Instead of being done on the Amazon website, it was done on the Mercado Libre website.

#### Files
- `meli_scraper.py`: Main script for scraping and writing to CSV.
- `meli_products_urls.csv`: CSV file containing URLs of Mercado Libre products to scrape.

#### Usage
1. Install dependencies using `pip install requests beautifulsoup4 tqdm`.
2. Populate the `meli_products_urls.csv` file with URLs of Mercado Libre products you want to scrape.
3. Run `python meli_scraper.py` to initiate scraping and generate the CSV output file.

#### Notes
- This script uses threading to improve scraping speed. Adjust `NO_THREADS` as needed for your setup.

---

### Project 3: web bot

#### Description
This project automates interactions with Trello using Selenium. It logs into Trello, navigates to a specific board, adds a task, and takes a screenshot of the page.

#### Changes Made
Custom implementation based on the original course material due to Trello source code changes since the course's release.

#### Files
- `trello_bot.py`: Main script for automating Trello interactions.
- `config.json`: Configuration file where personal data needs to be filled in to use the project.
- `chromedriver`: ChromeDriver executable required for Selenium (download the appropriate driver for your browser and OS).
- `downloads`: Folder where the screenshots are saved.

#### Usage
1. Install dependencies using `pip install selenium`.
2. Download the appropriate ChromeDriver for your browser and OS.
3. Populate the `config.json` file with your Trello username and password.
4. Run `python trello_bot.py` to start the automation.

#### Notes
- Ensure the `chromedriver` path is correctly set in the script.
- The script runs in headless mode by default. Remove `OP.add_argument('--headless')` if you want to see the browser in action.

