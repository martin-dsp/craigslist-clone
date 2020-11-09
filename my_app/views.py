from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    # POST = http protocol / get here is a method in Python.
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)