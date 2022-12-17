#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:05:23 2022

@author: susheel
"""

#text: this app will summarize any link you provide, within the following capabilities

#text: supported domains: Reddit

import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#link = input("Enter Reddit post link to summrize: ")

link = 'https://www.reddit.com/r/MaliciousCompliance/comments/ysarcg/apartment_manager_doesnt_take_cash_for_002_bill/'

url = link
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

with open('test_text_file.txt', 'w') as f:
    f.write(soup.prettify())
            
            
#print(soup.prettify())