#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://www.advokatsamfundet.se/Behover-du-advokat/Sok-advokat/Sokresultat/?positions=102001"
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.text)
divs = soup.find_all('div', {'class': "col-1"})
for div in divs:
	link = div.find("a")
	if link:
		#print(link.text)
		href = link["href"]
		sub_url = "https://www.advokatsamfundet.se" + href
		#print(sub_url)
		response = requests.get(sub_url)
		soup = BeautifulSoup(response.text)
		div_tag = soup.find_all("div", {'class': "space-5"})
		#if div_tag:
		#if (div_tag[0].text):
		#if (div_tag[1].text):		
		#if (div_tag[2].text):
		#if (div_tag[3].text):
		#if (div_tag[4].text):
		#if (div_tag[5].text):
		#if (div_tag[6].text):
		#if (div_tag[7].text):
		#print(div_tag[0].text)
		#print(div_tag[1].text)
		#print(div_tag[2].text)
		#print(div_tag[3].text)
		#print(div_tag[4].text)
		#print(div_tag[5].text)
		#print(div_tag[6].text)
		#print(div_tag[7].text)
		print(link.text + ";" + div_tag[0].text + ";" + div_tag[1].text + ";" + div_tag[2].text + ";" + div_tag[3].text + ";" + div_tag[4].text + ";" + div_tag[5].text + ";" + div_tag[6].text + ";" + div_tag[7].text)
