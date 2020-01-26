import re
import nltk  # For stopwords
import numpy as np
from PIL import Image  # To open image
from nltk.corpus import stopwords  # To import stopwords
from wordcloud import WordCloud, ImageColorGenerator  # To make WordCloud
from collections import Counter
from nltk.stem import WordNetLemmatizer

ls = []
file = open("English_Gita.txt","r", errors='ignore')
for line in file:
    try:
        line = line.strip()
        if line:
            ls.append(line)
    except Exception as err:
        print("Couldn't get that line")

text =''.join(ls)
text = text.lower()

#print(Counter(text.split()).most_common(3))

stopword_list = stopwords.words('english')
tokens = nltk.word_tokenize(text)
tokens = [token.strip() for token in tokens]
tokens_new = ' '.join([token for token in tokens if token not in stopword_list])

wordnet_lemmatizer = WordNetLemmatizer()
text_new = wordnet_lemmatizer.lemmatize(tokens_new)

print(len(text_new))
print(Counter(text_new.split()).most_common(25))

mask = np.array(Image.open("bg.jpg"))
image_colors = ImageColorGenerator(mask)
wc = WordCloud(background_color="#000f1a", max_words=500, width=1920, height=1080, mask=mask,
               random_state=1,collocations=True ).generate_from_text(text_new)
wc.recolor(color_func=image_colors)
wc.to_file('wordcloud_gita.png')

