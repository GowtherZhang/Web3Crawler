import json

str = '''
[{"name":"Bob", "gender":"male", "birth":"1992-10-18"},
{"name":"Selina", "gender":"female", "birth":"1995-10-18"}
]
'''

print(type(str))
data = json.loads(str)
print(data)
print(type(data))