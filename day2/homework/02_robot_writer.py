# coding: utf-8 

"""
HEMUPPGIFT 2
============
Skriv 290 notiser om arbetslösheten!

Jobba vidare på funktionen du skrev i förra hemläxan som skrev en 
nyhetstext om arbetslöshetsutvecklingen i en kommun.
Den här gången ska du skriva notiser om ALLA kommuner genom att loopa
genom en kommunlista.

BONUS:
Utveckla din write_story()-funktion så att den också 
använder categorize_unemployment() som vi skrev under lektionen.
"""

"""
Hämta in en lista med kommundata från filen unemployment.py
"""
from unemployment import data

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

""" Klistra in din egen write_story-funktion här
"""
def write_story(municipality, unemployment_2009, unemployment_2014):
    story = "Skriv en story!"

#for row in data:
#    print row
    # Skriv kod här!



#***************************************

from unemployment import data

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0
total_unemployment_rise = total_unemployment_2014 - total_unemployment_2009



def categorize_unemployment(unemployment):
    if unemployment < 5.0:
        return "låg"
    if unemployment >= 7.0:
        return "hög"
    return "medel"

for row in data:
    county = row["municipality"]
    no_job = row["unemployment_2014"]
    unemployment_rise = row["unemployment_2014"] - row["unemployment_2009"]
    if unemployment_rise < total_unemployment_rise:
        if unemployment_rise < 0:
            print("Arbetslösheten i %s är %s. Arbetslösheten i %s var år 2014 %s procent lägre än efter finanskrisen 2009. Den har gått ner från %s procent till %s procent. Utvecklingen för kommunen har varit lägre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (county, categorize_unemployment(no_job), row["municipality"], abs((row["unemployment_2014"]) - (row["unemployment_2009"])), row["unemployment_2009"], row["unemployment_2014"], total_unemployment_rise)
        else:
			if unemployment_rise == 0:
				print("Arbetslösheten i %s är %s. Arbetslösheten i %s var år 2014 samma som vid finanskrisen 2009. Den har stått stilla på %s procent. Utvecklingen för kommunen har varit lägre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (county, categorize_unemployment(no_job), row["municipality"], row["unemployment_2009"], total_unemployment_rise)
			else:
				if unemployment_rise > 0:
					print("Arbetslösheten i %s är %s. Arbetslösheten i %s var år 2014 %s procent högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent. Utvecklingen för kommunen har varit lägre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (county, categorize_unemployment(no_job), row["municipality"], abs((row["unemployment_2014"]) - (row["unemployment_2009"])), row["unemployment_2009"], row["unemployment_2014"], total_unemployment_rise)
	if unemployment_rise == total_unemployment_rise:
		print("Arbetslösheten i %s är %s. Arbetslösheten i %s var år 2014 %s procent högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent. Utvecklingen för kommunen var samma som i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (county, categorize_unemployment(no_job), row["municipality"], abs((row["unemployment_2014"]) - (row["unemployment_2009"])), row["unemployment_2009"], row["unemployment_2014"], total_unemployment_rise)
	if unemployment_rise > total_unemployment_rise:
		print("Arbetslösheten i %s är %s. Arbetslösheten i %s var år 2014 %s procent högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent. Utvecklingen för kommunen har varit högre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (county, categorize_unemployment(no_job), row["municipality"], abs((row["unemployment_2014"]) - (row["unemployment_2009"])), row["unemployment_2009"], row["unemployment_2014"], total_unemployment_rise)

    #print("Arbetslösheten i %s är %s" % (county, categorize_unemployment(no_job)))

""" Klistra in din egen write_story-funktion här

def write_story(municipality, unemployment_2009, unemployment_2014):
	unemployment_rise = unemployment_2014 - unemployment_2009
	if unemployment_rise < total_unemployment_rise:
		if unemployment_rise < 0:
			print("Arbetslösheten i %s var år 2014 %s procent lägre än efter finanskrisen 2009. Den har gått ner från %s procent till %s procent. Utvecklingen för kommunen har varit lägre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (municipality, abs(unemployment_2014 - unemployment_2009), unemployment_2009, unemployment_2014, total_unemployment_rise)
		else:
			if unemployment_rise == 0:
				print("Arbetslösheten i %s var år 2014 samma som vid finanskrisen 2009. Den har stått stilla på %s procent. Utvecklingen för kommunen har varit lägre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (municipality, unemployment_2009, total_unemployment_rise)
			else:
				if unemployment_rise > 0:
					print("Arbetslösheten i %s var år 2014 %s procent högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent. Utvecklingen för kommunen har varit lägre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (municipality, unemployment_2014 - unemployment_2009, unemployment_2009, unemployment_2014, total_unemployment_rise)
	if unemployment_rise == total_unemployment_rise:
		print("Arbetslösheten i %s var år 2014 %s procent högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent. Utvecklingen för kommunen var samma som i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (municipality, unemployment_2014 - unemployment_2009, unemployment_2009, unemployment_2014, total_unemployment_rise)
	if unemployment_rise > total_unemployment_rise:
		print("Arbetslösheten i %s var år 2014 %s procent högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent. Utvecklingen för kommunen har varit högre än i hela landet där arbetslösheten under samma tid vuxit med %s procentenheter.") % (municipality, unemployment_2014 - unemployment_2009, unemployment_2009, unemployment_2014, total_unemployment_rise)
"""

"""

def categorize_unemployment(unemployment):
    if unemployment < 5.0:
        return "låg"
    if unemployment >= 7.0:
        return "hög"
    return "medel"

for row in data:
    county = row["municipality"]
    no_job = row["unemployment_2014"]
    print("Arbetslösheten i %s är %s" % (county, categorize_unemployment(no_job)))
"""

#for row in data:
#    print row
    # Skriv kod här!


#total_unemployment_2009 = 5.9
#total_unemployment_2014 = 8.0

#total_unemployment_rise = total_unemployment_2014 - total_unemployment_2009


		#print("Arbetslösheten i %s var år 2014 %s högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent.") % (municipality, unemployment_2014 - unemployment_2009, unemployment_2009, unemployment_2014)

"""
=======
    text = "Gör mig till en notis"
    print("Nu har jag löst uppfiften!")
    print(text)
    # Skriv kod här!
>>>>>>> 0b75cc4a73af7947e0872f98e2a85a320a992abd

def print_header(pop1, pop2):
    if pop2 > pop1:
        if pop2 / pop1 > 1.1:
            print("Vi ökar mycket")
        else:
            print("Vi ökar")
    else:
        if pop2 == pop1:
            print("Vi står stilla")
        else:
            if pop2 / pop1 < 0.5:
                print("Vi sjunker rekordmycket")
            else:
                print("Vi minskar")


""" 
#Testa roboten!
"""

write_story("Stockholm", 7.1, 6.6) 
print("**************")

write_story("Kiruna", 7.6, 4.2) 
print("**************")

write_story("Lessebo", 9.5, 13.2) 
print("**************")

"""
#Källa: http://www.ekonomifakta.se/sv/Fakta/Regional-statistik/Din-kommun-i-siffror/
"""
"""
#write_story("Stockholm", 7.1, 6.6)
#write_story("Kiruna", 7.6, 7.6)
#write_story("Lessebo", 9.5, 13.2)