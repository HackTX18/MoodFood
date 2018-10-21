
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests



def index(request):
    return render(request, "index.html")