# -*- coding: utf-8 -*-

""" ÖVNING
"""

stockholm = {
    'unemployment_2009': 4.0,
    'unemployment_2014': 5.1
}

solna = {
    'unemployment_2009': 2.7,
    'unemployment_2014': 4.1
}


""" Hur många procentenheter har arbetslösheten stigit i Stockholm?
"""
print(stockholm["unemployment_2014"] - stockholm["unemployment_2009"])



""" Hur många procentenheter har arbetslösheten stigit i Solna?
"""
print(solna["unemployment_2014"] - solna["unemployment_2009"])


""" Hur mycket högra arbetslöshet hade Stockholm än Solna 2014?
"""
print(stockholm["unemployment_2014"] - solna["unemployment_2014"])
