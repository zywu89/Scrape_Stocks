import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#specify the url
quote_page = 'https://www.marketwatch.com/investing/index/spx'

#query the webpage and return the html
page = urllib.request.urlopen(quote_page)

#parse the html
soup = BeautifulSoup(page, 'html.parser')

#get the name
name_box = soup.find('h1', attrs={'class': 'company__name'})
name = name_box.text.strip()
print(name)

#get the index price
price_box = soup.find('h3', attrs = {'class': 'intraday__price'})
price = price_box.text
print(price)

#store data into a csv file
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])
