#-*- coding: utf-8 -*-
import miljopartiet
import requests
import BeautifulSoup

"""
print(miljopartiet.mps)
"""
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
	def emailify(name, domain):
	small_name = name.lower().replace(" ", ".").replace("ö", "o").replace("ä", "a").replace("å", "a").replace("é", "e").replace("Ö", "o")
	mail_address = small_name + "@" + domain
#	small_english_name = small_name + english_name
	print(mail_address)
#	first_name + last_name = name
#	small_english_name = name.lower().replace("ä", "a”)
   
"""