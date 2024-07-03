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


