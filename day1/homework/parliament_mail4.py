#-*- coding: utf-8 -*-
"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""

def emailify(name, domain):
	name_list = name.split(" ")
	new_name = ".".join(name_list)
	small_name = new_name.lower()
	english_name = small_name.replace("ö", "o").replace("ä", "a").replace("å", "a").replace("é", "e").replace("Ö", "o")
	mail_address = english_name + "@" + domain
	print(mail_address)
#	first_name + last_name = name
#	small_english_name = name.lower().replace("ä", "a”)
    

"""
Koden ska göra följande:
1) Ersätta mellanslag med punkter i namnet.
2) Göra alla tecken till små bokstäver
3) Ersätta specialtecken (å,ä,ö,é) med tecken som funkar
i en e-postadress.
4) Printa den kompletta adressen! 
"""
    # Skriv din kod här! 

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")
emailify("Camilla Waltersson Grönwall", "riksdagen.se")

"""
# Vi börjar med att spara ett namn i en variabel
name = "Jens Finnäs”

# Gör om till versaler
small_name = name.lower()

# Ersätt ä => a
english_name = name.replace("ä", "a”)

# Det går även att rada fler .lower() och .replace() på varandra
small_english_name = name.lower().replace("ä", "a”)
"""

