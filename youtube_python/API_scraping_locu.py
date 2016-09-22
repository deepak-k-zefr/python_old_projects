# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:01:22 2016

@author: p2admin
"""
import urllib
url=('https://api.locu.com/v1_0/venue/search/?country=United%20States&locality=Tempe&region=AZ&postal_code=85281&api_key=bb9b818ef53685ec699f79c2fdfd906dbd54eb2e')



from urllib.request import urlopen
with urlopen(url) as link:
    result = link.read()
    
import json
#print(json.load('https://api.locu.com/v1_0/venue/search/?country=United%20States&locality=Tempe&region=AZ&postal_code=85281&api_key=bb9b818ef53685ec699f79c2fdfd906dbd54eb2e'))