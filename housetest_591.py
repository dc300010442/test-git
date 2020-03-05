import requests
# from bs4 import BeautifulSoup

header= {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

url='https://www.591.com.tw/'

response= requests.get(url, headers=header)
print(response.text)

