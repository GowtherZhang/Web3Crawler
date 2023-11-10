from urllib.parse import urljoin

print(urljoin('https://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://caiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu,com?wd=abc','https://cuiqingcai.com/index.php'))
print(urljoin('https://www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com#comment','?category=2'))