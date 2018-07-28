#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:59:13 2018

@author: gyanesha
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import sqlite3
import json


link = "https://in.udacity.com/assets/localized-data/en-IN/catalogSchools.json?v=1"
#content = link.read()
#print(content)
#soup = BeautifulSoup(content,'lxml')
#print(soup)
course={}
hold = json.load(urlopen(link))
for data in hold['catalogSchools']:
    section = data['section']
    subsection = []
    for D in data['values']:
        title = D['title']
        withKey = D['matchCriteria']['withKey']
        subsection.append((title,withKey))
    course[section] = subsection
print(course)
#print(hold['catalogSchools'])
#print(type(hold))
#print(hold)
#m = json.loads(hold)
    