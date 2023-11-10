import requests
import logging

logging.basicConfig(level=logging.INFOm, format='%(asctime)s - %(levelname)s : %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info('scraping %s ...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.info('get error status_code %s while scraping %s', response.status_code, url)
    except:
        logging.error('error occurred while scraping %s', url, exc_info=True)

LIMIT = 10

def scrape_index(page):
    INDEX_URL.format(limit = LIMIT, offset = LIMIT * (page - 1))
    return scrape_api(INDEX_URL)

DETAIL_URL = 'https: // spa1.scrape.center / api / movie / {id}'

def scrape_detail(id):
    url = DETAIL_URL.format(id = id)
    return scrape_api(url)

TOTAL_PAGE = 10

def main():
    for page in range(TOTAL_PAGE):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)

if __name__  == '__main__':
    main()