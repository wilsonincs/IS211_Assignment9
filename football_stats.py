__author__ = 'wilsonincs'
import urllib2
import pprint as p
from bs4 import BeautifulSoup


"""Load the list of the top 20 players, including the player's position, team and total number of touchdowns."""


#create a variable that holds the link for the page stats
cbs_stats_url = "http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns"

openPage = urllib2.urlopen(cbs_stats_url) #load the page
readPage = BeautifulSoup(openPage.read()) #parse the page through beautifulsoup

soupImport = readPage.find_all('tr',{'align':'right'}) #create  table rows and center the data

player_statList = []  #create an empty list

for i in player_statList[:20]:
    name = i.contents[0].get_text()
    position = i.contents[1].get_text()
    touchdown = i.contents[6].get_text()
    player_statList.append((name,position,touchdown))


p.pprint(player_statList)





