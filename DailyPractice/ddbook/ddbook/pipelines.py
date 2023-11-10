# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DdbookPipeline:
    def process_item(self, item, spider):
        db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
        cursor = db.cursor()

        name = item["name"][0]
        introduction = item["introduction"][0]
        author = item["author"][0]
        price = item["price"][0].strip("￥")
        press = item["press"][0]
        time = item["time"][0].strip().strip('/')
        comment_num = item["comment_num"][0]

        cursor.execute(
              'insert into ddpython(name, introduction, author, price, press, time, comment_num) values (%s, %s, %s,%s,%s,%s,%s)',
              (name,introduction, author, price, press, time, comment_num)          
                       )
        db.commit()

        cursor.close()
        db.close()
        return item


