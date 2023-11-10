import requests
from pyquery import PyQuery as pq
import re
url = 'https://ssr1.scrape.center'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()

file = open('movie.txt', 'w', encoding='utf-8')
for item in items:
    name = item.find('a > h2').text()
    file.write(f"名称：{name}\n")
    categories = [item.text() for item in item.find('.categories button span').items()]
    file.write(f'类别：{categories}\n')
    published_at = item.find('.info:contains(上映)').text()
    file.write(f'上映时间：{published_at}\n')
    score = item.find('p.score').text()
    file.write(f'评分：(score)\n')
    file.write(f'{"=" * 50}\n')
file.close()