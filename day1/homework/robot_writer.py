# -*- coding: utf-8 -*-

""" Se robot_writer.md för instruktioner
"""

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

total_unemployment_rise = total_unemployment_2014 - total_unemployment_2009

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

		#print("Arbetslösheten i %s var år 2014 %s högre än efter finanskrisen 2009. Den har gått upp från %s procent till %s procent.") % (municipality, unemployment_2014 - unemployment_2009, unemployment_2009, unemployment_2014)

"""

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
write_story("Stockholm", 7.1, 6.6)
write_story("Kiruna", 7.6, 7.6)
write_story("Lessebo", 9.5, 13.2)
