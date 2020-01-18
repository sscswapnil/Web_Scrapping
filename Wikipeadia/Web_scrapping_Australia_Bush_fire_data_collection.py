# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:42:04 2020

@author: ssc
"""

import nltk 
import urllib
import bs4 as bs
import re
from nltk.corpus import stopwords
nltk.download('stopwords')

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Bushfires_in_Australia').read()

# parsing the data/creating the beautiful soup object
soup=bs.BeautifulSoup(source,'lxml')

# Fetching the data 
text=""
for paragraph in soup.find_all('p'):
    text +=paragraph.text
    
# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Preparing the dataset
+nltk.download('punkt')
SENT_DETECTOR = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
