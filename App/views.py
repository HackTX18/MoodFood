
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



def index(request):
    return render(request, "index.html")


# Temporary hard-coded site
SITE = "https://www.yelp.com/biz/mcdonalds-plano-22"
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