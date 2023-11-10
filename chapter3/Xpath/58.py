import requests
from lxml import etree
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s :%(message)s')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
url = 'https://sh.58.com/ershoufang/p1/?PGTID=0d200001-0000-2702-00ef-97239c9d1df0'

logging.info('scraping %s...', url)

data = pd.DataFrame(columns = ['Description', 'Total', 'Price'])

try:
    response = requests.get(url = url, headers = headers)
    if response.status_code == 200:
        # print(response.text)
        html = etree.HTML(response.text)
        div_list = html.xpath('//div[@class = "property" and @tongji_tag="fcpc_ersflist_gzcount"]/a/div[2]')
        for div in div_list:
            title = div.xpath('./div[1]/div[1]/h3/text()')
            total = div.xpath('./div[2]/p[1]/span[1]/text()')
            price = div.xpath('./div[2]/p[2]/text()')
            data = data.append({'Description':title, 'Total':total, 'Price':price},ignore_index=True)
    else:
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)

except requests.RequestException:
    logging.error('error occurred while scraping %s', url)

data.to_csv('58.csv',encoding='utf-8')




# div[2]/div[1]/div[1]/h3/text()

# div[3]/a/div[2]/div[1]/div[1]/h3