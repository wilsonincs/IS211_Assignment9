__author__ = 'wilsonincs'


import urllib2
from bs4 import BeautifulSoup

URL = "http://www.wunderground.com/history/airport/KNYC/2015/11/1/MonthlyCalendar.html"
PAGE = urllib2.urlopen(URL)


def get_temps(page):

    soup = BeautifulSoup(page.read())

    # finds each type of day class CSS
    x = soup.find_all('td', {'class': 'day '})
    y = soup.find_all('td', {'class': 'day todayBorder'})
    z = soup.find_all('td', {'class': 'day forecast'})


    day = 1
    for i in a:
        print "Day: " + str(day) + "  --- High: " + i.contents[3].text[10:14] + \
              "Low: " + i.contents[3].text[16:19]
        day += 1

    for i in b:
        print "Day: " + str(day) + "  --- High: " + i.contents[3].text[12:16] + \
              "Low: " + i.contents[3].text[18:21]
        day += 1

    for i in c:
        print "Day: " + str(day) + "  --- High: " + i.contents[3].text[12:16] + \
              "Low: " + i.contents[3].text[18:21]
        day += 1

if __name__ == "__main__":
    get_temps(PAGE)