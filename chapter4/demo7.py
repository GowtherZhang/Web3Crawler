import csv

with open('data2.csv', 'r', encoding='utf-8') as csvfile:
    for row in csv.reader(csvfile):
        print(row)