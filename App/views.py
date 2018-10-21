
from django.shortcuts import render
from django.http import HttpResponse
# from yelpreviewscraper import get_reviews
import json
import App.yelpreviewscraper as YPS

# part of speech dependencies
import re
import nltk

# word cloud graphic generator dependencies
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

import App.requestbusinesses as RQB
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

def index(request):
    return render(request, "index.html")

location_list = [20]

def search(request):
    try:
        location_list = RQB.query_api('fuck', 'New York, NY', '', '')
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

    SITE = location_list[0]
    REVIEWSTRING = YPS.get_reviews(SITE)

    print(REVIEWSTRING)

    listOfAdjectives = []

    try:

        tokenized = nltk.word_tokenize(REVIEWSTRING[1])
        tagged = nltk.pos_tag(tokenized)
        for word in tagged:
            if('J' in (word[1])):
                listOfAdjectives.append(word[0])

    except Exception as e:
            print(str(e))


    text = ''
    for word in listOfAdjectives:
        text = text + ' ' + word

    wc = WordCloud().generate(text)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    return HttpResponse("<p>" + location_list[0] + "</p>")
# Temporary hard-coded site
