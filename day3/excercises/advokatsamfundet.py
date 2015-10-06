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
	#print(link)
	if link:
		href = link["href"]
		sub_url = "https://www.advokatsamfundet.se" + href
		print(sub_url)


"""
print(sub_url)



	link = soup.find("div", {'class': "lead"})
	#else:
	#	description = ""
	print(mp_name.text)
	if link:
		description = link.find("p")
		print(description.text)
"""
"""

	link = 
	url = "https://www.advokatsamfundet.se/" + link




def slugify(argument):
	slug = argument.lower()\
		.replace(" ", "-")\
		.replace("ö", "o")\
		.replace("ä", "a")\
		.replace("å", "a")\
		.replace("Å", "a")\
		.replace("é", "e")\
		.replace("Ö", "o")\
		.replace("ü", "u")
	return slug

for argument in miljopartiet.mps:
	changed_name = slugify(argument)
	url = "http://www.mp.se/om/" + changed_name
	# = response.text
	response = requests.get(url)
	soup = BeautifulSoup.BeautifulSoup(response.text)
#response.text innehåller html-koden
	mp_name = soup.find("h1")
	#mp_uppdrag = soup.find('div', {'class': "lead"})
	mp_email = soup.find('a', {'class': "email"})
	mp_mobile = soup.find('a', {'class': "tel"})
	div_tagg = soup.find("div", {'class': "lead"})
	#else:
	#	description = ""
	print(mp_name.text)
	if div_tagg:
		description = div_tagg.find("p")
		print(description.text)
	#print(mp_uppdrag.text)
	if mp_email:
		print(mp_email.text)
	if mp_mobile:
		print(mp_mobile.text)
	#print(slugify(argument))

	"""