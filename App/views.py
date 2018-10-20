from django.shortcuts import render
from django.http import HttpResponse
import json
from pprint import pprint
# Create your views here.

with open("templates/yelp_academic_dataset_review.json") as f:
    data = json.load(f)
    print(data)

def index(request):
    return HttpResponse("Hello world")