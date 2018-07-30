from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from .models import *
import sqlite3
import urllib.request,json


def scraping_test(request):
    link = "https://in.udacity.com/assets/localized-data/en-IN/catalogSchools.json?v=1"
    categories={}
    hold = json.loads(urllib.request.urlopen(link).read().decode())
    for data in hold['catalogSchools']:
        section = data['section']
        subsection = []
        for D in data['values']:
            title = D['title']
            withKey = D['matchCriteria']['withKey']
            subsection.append((title,withKey))
        categories[section] = subsection
    print(categories)
    for section in categories:
        try:
            category = Category.objects.get(name=section)
            for s in categories[section]:
                try:
                    category.subcategory_set.get(name=s[0])
                except Subcategory.DoesNotExist:
                    subcategory = Subcategory.objects.create(name=s[0])
                    category.subcategory_set.add(subcategory)
        except Category.DoesNotExist:
            if len(section)!=0:     
                category = Category.objects.create(name=section)
                for s in categories[section]:
                    category.subcategory_set.create(name=s[0])
    return HttpResponse("check terminal")