from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://indianexpress.com/section/india/').text

soup = BeautifulSoup(source, 'lxml')


csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file).writerow(['headline', 'summary'])


for article in soup.find_all('div', class_='articles'):

    headline = article.find('h2', class_='title').text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

    csv_writer.writerow([headline, summary])

csv_file.close()


