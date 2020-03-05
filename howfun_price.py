import requests
from bs4 import BeautifulSoup


source = requests.get('https://sale.591.com.tw/home/house/detail/2/6993238.html').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('container')

headline = article.h1.text

print(headline)

# print(article)

