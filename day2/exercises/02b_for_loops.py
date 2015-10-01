# -*- coding: utf-8 -*-


unicorn_list = [
    "Joachim Kerpner",
    "Nina Svanberg",
    "Johan Ronge",
    "Christian Holmén",
    "Fredrik Laurin",
    "Olle Carlsson",
    "Lolo Tode Palm",
    "Martin Jönsson"
]

"""
ÖVNING:
Använd funktionen len(), som funkar på både strängar och listor,
och räkna ut hur många deltagare som har långa respektive korta namn.
"""

long_names_counter = 0
short_names_counter = 0
total_unicorns = len(unicorn_list)
#counter = 1

#print("Nu börjar programmet! Låt oss räkna långa och korta namn.")

for unicorn in unicorn_list:
	name_length = len(unicorn)
	if name_length >= 14:
		long_names_counter = long_names_counter + 1
	else:
	    if name_length <= 13:
		    short_names_counter = short_names_counter + 1

print("%s av %s enhörningar har korta namn" % (short_names_counter, total_unicorns))

print("%s av %s enhörningar har långa namn." % (long_names_counter, total_unicorns))

"""
for unicorn in unicorns:
    counter = counter + 1
    print ("%s. %s" %(counter, unicorn))
    """
