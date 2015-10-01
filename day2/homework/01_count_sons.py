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
	if "son" in row["name"]:
		counter_son_names = counter_son_names + 1	

print("Av %s ledamöter har %s son-namn" %(total_number_of_mps, counter_son_names))

counter_party_SD = 0
counter_son_names_SD = 0
for row in data:
	if "SD" in row["party"]:
		counter_party_SD = counter_party_SD + 1
		if "son" in row["name"]:
			counter_son_names_SD = counter_son_names_SD + 1
counter_percent_SD = float(counter_son_names_SD) / float(counter_party_SD) * 100

print("%s av %s ledamöter i SD har son-namn, det vill säga %s procent." %(counter_son_names_SD, counter_party_SD, counter_percent_SD))

counter_party_FP = 0
counter_son_names_FP = 0
for row in data:
	if "FP" in row["party"]:
		counter_party_FP = counter_party_FP + 1
		if "son" in row["name"]:
			counter_son_names_FP = counter_son_names_FP + 1
counter_percent_FP = float(counter_son_names_FP) / float(counter_party_FP) * 100

print("%s av %s ledamöter i FP har son-namn, det vill säga %s procent." %(counter_son_names_FP, counter_party_FP, counter_percent_FP))

counter_party_KD = 0
counter_son_names_KD = 0
for row in data:
	if "KD" in row["party"]:
		counter_party_KD = counter_party_KD + 1
		if "son" in row["name"]:
			counter_son_names_KD = counter_son_names_KD + 1
counter_percent_KD = float(counter_son_names_KD) / float(counter_party_KD) * 100

print("%s av %s ledamöter i KD har son-namn, det vill säga %s procent." %(counter_son_names_KD, counter_party_KD, counter_percent_KD))

counter_party_MP = 0
counter_son_names_MP = 0
for row in data:
	if "MP" in row["party"]:
		counter_party_MP = counter_party_MP + 1
		if "son" in row["name"]:
			counter_son_names_MP = counter_son_names_MP + 1
counter_percent_MP = float(counter_son_names_MP) / float(counter_party_MP) * 100

print("%s av %s ledamöter i MP har son-namn, det vill säga %s procent." %(counter_son_names_MP, counter_party_MP, counter_percent_MP))

counter_party_M = 0
counter_son_names_M = 0
for row in data:
	if "M" in row["party"]:
		counter_party_M = counter_party_M + 1
		if "son" in row["name"]:
			counter_son_names_M = counter_son_names_M + 1
counter_percent_M = float(counter_son_names_M) / float(counter_party_M) * 100

print("%s av %s ledamöter i M har son-namn, det vill säga %s procent." %(counter_son_names_M, counter_party_M, counter_percent_M))

counter_party_C = 0
counter_son_names_C = 0
for row in data:
	if "C" in row["party"]:
		counter_party_C = counter_party_C + 1
		if "son" in row["name"]:
			counter_son_names_C = counter_son_names_C + 1
counter_percent_C = float(counter_son_names_C) / float(counter_party_C) * 100

print("%s av %s ledamöter i C har son-namn, det vill säga %s procent." %(counter_son_names_C, counter_party_C, counter_percent_C))

counter_party_V = 0
counter_son_names_V = 0
for row in data:
	if "V" in row["party"]:
		counter_party_V = counter_party_V + 1
		if "son" in row["name"]:
			counter_son_names_V = counter_son_names_V + 1
counter_percent_V = float(counter_son_names_V) / float(counter_party_V) * 100

print("%s av %s ledamöter i V har son-namn, det vill säga %s procent." %(counter_son_names_V, counter_party_V, counter_percent_V))

counter_party_S = 0
counter_son_names_S = 0
for row in data:
	if "S" in row["party"]:
		counter_party_S = counter_party_S + 1
		if "son" in row["name"]:
			counter_son_names_S = counter_son_names_S + 1
counter_percent_S = float(counter_son_names_S) / float(counter_party_S) * 100

print("%s av %s ledamöter i S har son-namn, det vill säga %s procent." %(counter_son_names_S, counter_party_S, counter_percent_S))

