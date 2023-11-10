from selenium import webdriver
from selenium.webdriver.common.by import By
import logging 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
PAGE_TOTAL = 10

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging']) #禁用DevTools
option.add_experimental_option('detach', True) # 不自动关闭窗口
option.add_argument('--start-maximized')

browser = webdriver.Chrome(options=option)
wait = WebDriverWait(browser, TIME_OUT)

def scrape_page(url, condition, locator):
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scrping %s', url, exc_info=True)

def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))

def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)

def scrape_detail(url):
    scrape_page(url=url, condition=EC.visibility_of_all_elements_located, locator=(By.TAG_NAME,'h2'))

def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.XPATH, '//a[@class="name"/h2/text()]')
    category = browser.find_element(By.XPATH, '//div[@class="categories"]//button/span//text()')
    cover = browser.find_element(By.PATH, '//img[@class="cover"]/@src')
    score = browser.find_element(By.PATH, '//div/p[@class="score/text()"]')
    drama = browser.find_element(By.PATH, '//div[@class="drama"]/p/text()"]')
    return {
        'url':url,
        'name':name,
        'category':category,
        'cover':cover,
        'score':score,
        'drama':drama
    }
    
def main():
    try:
        for page in range(1, PAGE_TOTAL + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in detail_urls:
                 logging.info('detail urls %s', detail_urls)
                 scrape_detail(detail_url)
                 detail_data = parse_detail()
                 logging.info('detail data %s', detail_data)
           
    finally:
        browser.close()

main()