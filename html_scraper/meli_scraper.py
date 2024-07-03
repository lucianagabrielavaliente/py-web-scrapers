from datetime import datetime
import requests
import csv
import bs4
import concurrent.futures
from tqdm import tqdm

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'es-LA, es;q=0.5',
}
NO_THREADS = 10

def get_page_html(url):
    res = requests.get(url = url, headers=REQUEST_HEADER)
    return res.content

def get_product_price(soup):
    meta_tag = soup.find('meta', attrs={'itemprop': 'price', 'content': True})
    price_value = meta_tag['content']
    try:
        return float(price_value)
    except ValueError:
        print("Value Obtained For Price Could not Be Returned As Float")
        exit()

def get_product_title(soup):
    h1_tag = soup.find('h1', class_='ui-pdp-title')
    title_text = h1_tag.text.strip()
    return title_text

def extract_product_info(url, output):
    product_info = {}
    #print(f'Scraping URL:{url}')
    html = get_page_html(url=url)
    soup = bs4.BeautifulSoup(html, "html5lib")
    product_info['title'] = get_product_title(soup)
    product_info['price'] = get_product_price(soup)
    output.append(product_info)

if __name__ == "__main__":
    product_data = []
    urls = []
    with open('meli_products_urls.csv', newline='') as csvfile:
        urls = list(csv.reader(csvfile, delimiter=','))
    with concurrent.futures.ThreadPoolExecutor(max_workers=NO_THREADS) as executor:
        for wkn in tqdm(range(0, len(urls))):
            executor.submit(extract_product_info, urls[wkn][0],product_data)
    current_date = datetime.today().strftime("%m-%d-%Y")
    output_file_name = f'output-{current_date}.csv'
    with open(output_file_name,'w', newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(product_data[0].keys())
        for product in product_data:
            writer.writerow(product.values())