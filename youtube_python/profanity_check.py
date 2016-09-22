# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 01:35:25 2016

@author: p2admin
"""
import urllib
import requests


def check_profanity(text_to_check):
    connection =  requests.get("http://www.wdyl.com/profanity?q={}".format(text_to_check))
    output=connection.read()
    print(output)
    connection.close()
def read_text():
    quotes=open(r"C:\Users\p2admin\Downloads\movie_quotes.txt")
    contents=quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

read_text()
    