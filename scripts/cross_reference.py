import re
import nltk  # For stopwords
import numpy as np
from PIL import Image  # To open image
from nltk.corpus import stopwords  # To import stopwords
from wordcloud import WordCloud, ImageColorGenerator  # To make WordCloud
from collections import Counter
from nltk.stem import WordNetLemmatizer

ls_gita = []
file_gita = open("English_Gita.txt","r", errors='ignore')
for line in file_gita:
    try:
        line = line.strip()
        if line:
            ls_gita.append(line)
    except Exception as err:
        print("Couldn't get that line")

text_gita = ''.join(ls_gita)
text_gita = text_gita.lower()

stopword_list = stopwords.words('english')
tokens_gita = nltk.word_tokenize(text_gita)
tokens_gita = [token.strip() for token in tokens_gita]
tokens_new_gita = [token for token in tokens_gita if token not in stopword_list]
words_gita = [word for word in tokens_new_gita if word.isalpha()]
#print(words_gita)

ls_maha = []
file_maha = open("English_Mahabharat.txt","r", errors='ignore')
for line in file_maha:
    try:
        line = line.strip()
        if line:
            ls_maha.append(line)
    except Exception as err:
        print("Couldn't get that line")

text_maha = ''.join(ls_maha)
text_maha = text_maha.lower()

stopword_list = stopwords.words('english')
tokens_maha = nltk.word_tokenize(text_maha)
tokens_maha = [token.strip() for token in tokens_maha]
tokens_new_maha = [token for token in tokens_maha if token not in stopword_list]
words_maha = [word for word in tokens_new_maha if word.isalpha()]

common = {}
for i in words_maha:
    common[i] = words_gita.count(i)

freq = sorted(common.items(), key = lambda x: x[1], reverse=True)

print(freq)


