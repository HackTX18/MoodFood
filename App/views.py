
from django.shortcuts import render
from django.http import HttpResponse
from yelpreviewscraper import get_reviews
import json
import requests



def index(request):
    main()
    return HttpResponse("Hello world")

# Temporary hard-coded site
SITE = "https://www.yelp.com/biz/mcdonalds-plano-22"
REVIEWSTRING = get_reviews(SITE)
print(REVIEWSTRING)