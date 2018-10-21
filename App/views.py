
from django.shortcuts import render
from django.http import HttpResponse
#from yelpreviewscraper import get_reviews
import json
import requests
import App.yelpreviewscraper as YPS


def index(request):
    return render(request, "header.html")

# Temporary hard-coded site
'''ITE = "https://www.yelp.com/biz/mcdonalds-plano-22"
REVIEWSTRING = YPS.get_reviews(SITE)
print(REVIEWSTRING)
'''