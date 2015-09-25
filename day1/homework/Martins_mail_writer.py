#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""

def emailify(name, domain):
    formated_name = name.lower()\
        .replace(" ", ".")\
        .replace("å", "a")\
        .replace("ä", "a")\
        .replace("ö", "o")\
        .replace("é", "e")\
        .replace("Ö", "o")

    email = formated_name + "@" + domain
    print(email)

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")