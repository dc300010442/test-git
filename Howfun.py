from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://news.housefun.com.tw/news').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('howfun_scrape.csv','w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline','summary'])


for article in soup.find_all('article'):



        headline = article.h2.a.text
        print(headline)

        summary = article.find('div', class_='info').text
        print(summary)

        # vid_src = article.find('class_='youtube-player')

        print()

        csv_writer.writerow([headline,summary])

csv_file.close()