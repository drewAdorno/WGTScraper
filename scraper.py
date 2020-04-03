from bs4 import BeautifulSoup
import requests
import bs4
import re
import sys
import pprint

name=sys.argv[1]
page = requests.get(f"http://www.wgt.com/members/{name[0:10]}/default.aspx")
soup = bs4.BeautifulSoup(page.content, 'lxml')
pp = pprint.PrettyPrinter(indent=4)

def extract(id):
    temp=soup.find(id=f'ctl00_ctl00_ctl00_body_bodyContent_{id}')
    temp=re.sub('<[^<]+?>', '', str(temp))
    return temp
player={
'Name':name,
'Level':extract('playerLevel'),
'Tier':extract('playerTier'),
'AvgScore':extract('playerAvgScore'),
'Status':extract('playerStatusLabel'),
'JoinDate':extract('playerMemberSince'),
'Earnings':extract('playerCareerEarnings'),
'CountryClub':extract('CountryClubURL'),
}

# for key in player:
#     print(f'{key}: {player[key]}')
print(player)
pp.pprint(player)