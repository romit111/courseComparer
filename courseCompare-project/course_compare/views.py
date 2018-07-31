from django.shortcuts import render,redirect
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from .models import *
import sqlite3
import urllib.request,json
from .forms import SignupForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request,'home.html')

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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
