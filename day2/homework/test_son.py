#coding: utf-8
#-*- coding: utf-8 -*-
from riksdagsledamoter import data
"""
HEMUPPGIFT 1
============
Hur många riksdagsledamöter har ett son-namn?

1) Loopa listan med riksdagsledamöter
2) Kolla om personen har ett "son"-namn
3) Räkna många riksdagsledamöter som har son-namn.

Bonus:
 Räkna hur stor andel av ledamöterna i varje parti som har son-namn.

Den översta raden (from ... import ...) hämtar en lista med riksdagsledamöter
från riksdagsledamoter.py.

"""

counter_son_names = 0
total_number_of_mps = len(data)
counter_party = 0


for row in data:
	last_characters = row["name"][-3:]
	print last_characters
	print row["name"]

"""

	if "son" in row["name"]:
		counter_son_names = counter_son_names + 1	

print("Av %s ledamöter har %s son-namn" %(total_number_of_mps, counter_son_names))
"""
