import re

content = '54aK54b4nln6kj4bql'
result = re.sub('\d+', '', content)
print(result)