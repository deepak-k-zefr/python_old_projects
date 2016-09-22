# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:25:10 2016

@author: p2admin
"""

from bs4 import BeautifulSoup
import urllib.request
file=open('royalNavyShip.txt','w')
url = 'http://wikipedia.org/wiki/List_of_ship_names_of_the_Royal_Navy_'
wiki_html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(wiki_html,'lxml')
links=soup.find_all('a')
ship_urls = ['(A)','(B)','(C)','(D-F)','(G-H)','(I-L)','(M-N)','(O-Q)','(R-T)','(U-Z)']
for ship in ship_urls:
    for link in links:
        title= str(link.get('title'))
        if (title.startswith('HMS')):
            # print(title)
            file.write(title)
            file.write('\n')
