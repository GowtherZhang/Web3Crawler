import requests
import logging
import multiprocessing
import pymongo

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
      logging.info('scraping %s...', url)
      try:
            response = requests.get(url)
            if response.status_code == 200:
                  return response.json()
            logging.error('get invalid status code %s while scraping %s', response.status_code, url)
      except requests.RequestException:
            logging.error('error occurred while scraping %s', url, exc_info=True)

LIMIT = 10

def scrape_index(page):
      url = INDEX_URL.format(limit = LIMIT, offset=LIMIT * (page - 1))
      return scrape_api(url)

DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

def scrape_detail(id):
      url = DETAIL_URL.format(id=id)
      return scrape_api(url)

TOTAL_PAGE = 10

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_CONNECTION_NAME = 'movies'
#定义MongoDB连接的基本信息
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

'''调用upsert_one方法，第一个参数是查询条件，根据name进行查询，第二个参数是对象本身，就是所有的数据，用$操作符表示更新操作，
第三个参数upsert设置为True,表示存在即更新，不存在即插入'''
def save_data(data):
      collection.update_one(
            {'name':data.get('name')},
            {'$set':data},
            upsert=True)

def main(page):
      index_data = scrape_index(page)
      for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)
            logging.info('data saved successfully')

if __name__ == '__main__':
      pool = multiprocessing.Pool()
      pages = range(TOTAL_PAGE)
      pool.map(main, pages)
      pool.close()
      pool.join()