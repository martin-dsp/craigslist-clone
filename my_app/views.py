from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.api import post
# 띄어쓰기 같은 거 핸들링해줌!
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = "https://losangeles.craigslist.org/search/?query={}"

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    # POST = http protocol / get here is a method in Python.
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get('https://losangeles.craigslist.org/search/sss?query=cat+tower')
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find('a', {'class': 'result-title hdrlnk'}).text
        post_url = post.find('a').get('href')
        
        if post.find(class_='result-price'):
            post_price = post.find('span', {'class': 'result-price'}).text
        else:
            post_price = 'N/A'    
        final_postings.append((post_title, post_url, post_price))
            

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings, 
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)