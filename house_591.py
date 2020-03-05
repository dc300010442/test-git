
from bs4 import BeautifulSoup
header= {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

# url='https://rent.591.com.tw/rent-detail-8920845.html'

import requests
import json

res= requests.get('https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=3&firstRow=0&totalRows=42171&timestamp=1583397908643')
# data= json.loads(res.text)

print(res.text)

# print(data)