from bs4 import BeautifulSoup
import requests
import nltk
import re
import pandas as pd
import xlrd

def get_url():

    excel_file = 'AranyaKanda.xlsx'
    df = pd.read_excel(excel_file,header=2,usecols=['Verses'])
    values = df.values.tolist()
    number_of_verses = [item for sublist in values for item in sublist]

    sarga_number = 1
    number_of_chapters = 75
    j = 1

    text = ''

    file = open("aranyakanda_english_intro.txt","w",encoding="utf-8")

    while number_of_chapters >= sarga_number:
        ls = []
        url = requests.get(f"http://www.valmikiramayan.net/utf8/aranya/sarga{sarga_number}/aranyasans{sarga_number}.htm")
        soup = BeautifulSoup(url.content, 'html.parser')

        match = soup.findAll(class_='txt')
        match = str(match)
        #print(match)
        tags = re.compile(r'<[^>]+>')
        match = tags.sub('', match)
        ls.append(match)

        text = ' '.join(ls)
        text = text.replace('[', '')
        text = text.replace(']', '')
        file.write('Chapter: ' + str(j))
        file.write('\n')
        file.write(text)
        file.write('\n\n')

        del ls

        j += 1
        sarga_number += 1
        print(sarga_number)

get_url()