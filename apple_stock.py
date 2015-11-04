__author__ = 'wilsonincs'

"""Display the price and date at closing for the apple stock"""


import urllib2
from bs4 import BeautifulSoup
import pprint as p


url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

stock = soup.find_all('tr')

closing_data = []
for i in stock:
    if len(i.find_all('td', {'class': 'yfnc_tabledata1', 'align': 'right'})) == 7:
        date = i.contents[0].get_text()
        close = i.contents[6].get_text()
        closing_data.append((date, close))

p.pprint(closing_data)