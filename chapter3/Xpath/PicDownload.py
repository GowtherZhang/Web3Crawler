from lxml import etree
import os
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
url = 'http://pic.netbian.com/4kmeinv/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# response.encoding = 'utf-8'
html = etree.HTML(response.text)

if not os.path.exists('./Piclibs'):
    os.mkdir('./Piclibs')

li_list = html.xpath('//ul[@class="clearfix"]/li')
for li in li_list:
    img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    #中文乱码的通用解决办法
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    # print(img_name, img_src)
    img_data = requests.get(url=img_src, headers=headers).content
    logging.info('Downloading %s', img_name)
    with open('./Piclibs/'+img_name, 'wb') as fp:
        fp.write(img_data)