import csv

with open("data.csv", 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':"10005", "name":"张常常", "age":24})