from urllib import urlopen
from bs4 import BeautifulSoup

# html = urlopen('https://www.cnblogs.com/xiaodf/p/6277761.html').read().decode('utf-8')
html = open('/Users/zhangdi/Desktop/test.html', 'r')

soup = BeautifulSoup(html, features='html.parser')

a = soup.find_all('a')

cc = [l.get_text() for l in a if ('href' in l.attrs.keys())]
print(cc)
