
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests



def index(request):
    main()
    return HttpResponse("Hello world")