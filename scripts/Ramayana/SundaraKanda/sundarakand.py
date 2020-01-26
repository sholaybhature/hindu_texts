from bs4 import BeautifulSoup
import requests
import nltk
import re
import pandas as pd
import xlrd
import numpy as np
from PIL import Image  # To open image
from wordcloud import WordCloud, ImageColorGenerator  # To make WordCloud
from collections import Counter
import os
from cltk.stop.sanskrit.stops import STOPS_LIST
from cltk.tokenize.sentence import TokenizeSentence
from cltk.tokenize.sanskrit.word import WordTokenizer
from collections import defaultdict
import collections

def get_url():

    excel_file = 'SundaraKanda.xlsx'
    df = pd.read_excel(excel_file,header=2,usecols=['Verses'])
    values = df.values.tolist()
    number_of_verses = [item for sublist in values for item in sublist]
    #print(number_of_verses)

    sarga_number = 1
    number_of_chapters = 68
    j = 0

    text = ''

    ls = []
    ls_hindi = []
    ls_final =[]

    file = open("sundarakanda.txt","w",encoding="utf-8")

    while number_of_chapters >= sarga_number:
        url = requests.get(f"http://www.valmikiramayan.net/utf8/sundara/sarga{sarga_number}/sundarasans{sarga_number}.htm")
        soup = BeautifulSoup(url.content, 'html.parser')


        for k in range(0,number_of_verses[j]):
            try:
                match = soup.findAll(class_='SanSloka')[k]
                match = str(match)
                tags = re.compile(r'<[^>]+>')
                match = tags.sub('', match)

                ls.append(match)
            except (IndexError,ValueError):
                pass
        j += 1
        sarga_number += 1
        print(sarga_number)

    for letter in ls:
        if not re.search(r'[a-zA-Z]', letter):
            ls_hindi.append(letter)


    text = ' '.join(ls_hindi)
    text.strip(' ')
    text = text.replace('\n\n','')
    #print(text)
    re_text = (re.sub('[०१२३४५६७८९\\n\\r\|\-]+', '', text))
    #print(re_text)
    tokenizer = TokenizeSentence('sanskrit')

    tokens_ls = []
    for i in re_text.split():
        if len(i) > 3:
            tokens_re = tokenizer.tokenize(i)
            tokens_ls.append(tokens_re)

    tokens = [item for sublist in tokens_ls  for item in sublist]

    text_new = ([token for token in tokens if token not in STOPS_LIST])
    d = defaultdict(int)
    for i in text_new:
        d[i] += 1

    #print(len(text_new))

    file.write(text)

    mask = np.array(Image.open("bg_1.jpg"))
    image_colors = ImageColorGenerator(mask)
    wc = WordCloud(font_path="‪C:\\Users\\BB\\Desktop\\Sanskrit2003.ttf", background_color="#000000", max_words=150,
                   width=1920, height=1080, mask=mask,
                   random_state=1).fit_words(d)
    wc.recolor(color_func=image_colors)
    wc.to_file('wordcloud_sundara.png')

get_url()