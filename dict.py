# -*- coding: utf-8 -*-

import requests
import re
import collections


URL = "http://www.diki.pl/slownik-angielskiego/?q="
FILE = 'dict'

def readWordsFromFile():
    words = []

    with open(FILE, 'r') as f:
        for line in f:
            if line != '\n':
                words.append(line.strip())

    return words

def prepareUrl(word):
    return URL + word.strip()

def prepareReg():
    pattern = r'<span class="hw">(.*?)</span>'
    reg = re.compile(pattern, re.DOTALL | re.IGNORECASE)

    return reg

def getMeaning(word):
    req = requests.get(prepareUrl(word))
    req.encoding = 'utf-8'
    reg = prepareReg()
    finds = reg.findall(req.text)

    if len(finds) == 0:
        return "No translation"
    elif len(finds) == 1:
        return finds[0].encode('utf-8')
    else:
        return finds[1].encode('utf-8')

for counter, word in enumerate(readWordsFromFile()):
    meaning = str(getMeaning(word))
    pos = meaning.find('<')

    print str(counter) + '. ' + word + ' -- > ' + meaning[:pos] 
