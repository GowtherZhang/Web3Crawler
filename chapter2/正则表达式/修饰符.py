import re

content = '''Hello 1234567 World_this
 is a Regex Demo'''
result = re.match('^He.*?(\d+).*Demo$', content, re.S)
print(result)
print(result.group(1))