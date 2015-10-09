#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://www.riksdagen.se/sv/ledamoter-partier/Hitta-ledamot/Bokstavsordning/"
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.text)
dts = soup.find_all('dt')
for div in dts:
	link = div.find("a")
	print(link.text)
divs = soup.find_all('dd', {'class': "small"})
for divfact in divs:
	print(divfact.text)	
	#print(link.text + ";" + divfact.text)

"""

url = "http://www.riksdagen.se/sv/ledamoter-partier/Hitta-ledamot/Bokstavsordning/"
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.text)
dts = soup.find_all('dt')
for div in dts:
	link = div.find("a")
	print(link.text)
divs = soup.find_all('dd', {'class': "small"})
for divfact in divs:
	print(divfact.text)	

"""