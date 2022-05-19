#!/usr/bin/env python3

from collections import Counter
from collections import defaultdict
import re
import requests
import bs4
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import unicodedata
import sys
import numpy as np

def main():
    url = "whatever.html"
    soup = bs4.BeautifulSoup(url, 'html.parser')
    p_elems = [element.text for element in soup.find_all("p")]
    speech = ''.join(p_elems)

    token = word_tokenize(speech)
    f_speech_no_s = remove_stopwords(token)
    speech_no_p = remove_punctuation(f_speech_no_s)

    #readable speech
    final_speech = ' '.join(speech_no_p)

    #dicts
    tagged_token = dict(pos_tag(token))
    count = Counter(speech_no_p)
    max_count = dict()
    for key,value in count.items():
            if int(value) >= 5:
                max_count[key] = value

    final_d = defaultdict(list)

    for i in (max_count, tagged_token):
        for key, value in i.items():
            final_d[key].append(value)



    #readable
    read_val = sorted(max_count, key=max_count.get, reverse=True)
    tagged_max = dict(pos_tag(read_val))

    #print(read_val)
    print(tagged_max)

def remove_punctuation(text):
    punct = dict.fromkeys(i for i in range(sys.maxunicode)
                          if unicodedata.category(chr(i)).startswith('P'))
    text_no_p = [string.translate(punct) for string in text]
    return text_no_p

def remove_stopwords(token):
    stop_words = stopwords.words('english')
    stop_token = [word for word in token if word not in stop_words]
    return stop_token

if __name__ == '__main__':
    main()
