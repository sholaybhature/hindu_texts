from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

import matplotlib.font_manager as mfm

font_path = "‪C:\\Users\\BB\\Desktop\\Bold.ttf"
font_path = font_path.lstrip('\u202a')
prop = mfm.FontProperties(fname=font_path)

file = open('ramayana.txt', encoding='utf-8').read()

COLOR = {'amaranth': '#E52B50', 'amber': '#FFBF00', 'amethyst': '#9966CC', 'apricot': '#FBCEB1',
         'aquamarine': '#7FFFD4', 'azure': '#007FFF', 'baby blue': '#89CFF0', 'beige': '#F5F5DC', 'black': '#000000',
         'blue': '#0000CD', 'blue-green': '#0095B6', 'blue-violet': '#8A2BE2', 'blush': '#DE5D83', 'bronze': '#CD7F32',
         'brown': '#964B00', 'burgundy': '#800020', 'byzantium': '#702963', 'carmine': '#960018', 'cerise': '#DE3163',
         'cerulean': '#007BA7', 'champagne': '#F7E7CE', 'chartreuse green': '#7FFF00', 'chocolate': '#7B3F00',
         'cobalt blue': '#0047AB', 'coffee': '#6F4E37', 'copper': '#B87333', 'coral': '#FF7F50', 'crimson': '#DC143C',
         'cyan': '#00FFFF', 'desert sand': '#EDC9Af', 'electric blue': '#7DF9FF', 'emerald': '#50C878',
         'erin': '#00FF3F', 'gold': '#FFD700', 'gray': '#808080', 'green': '#00FF00', 'harlequin': '#3FFF00',
         'indigo': '#4B0082', 'ivory': '#FFFFF0', 'jade': '#00A86B', 'jungle green': '#29AB87', 'lavender': '#B57EDC',
         'lemon': '#FFF700', 'lilac': '#C8A2C8', 'lime': '#BFFF00', 'magenta': '#FF00FF', 'magenta rose': '#FF00AF',
         'maroon': '#800000', 'mauve': '#E0B0FF', 'navy blue': '#000080', 'ochre': '#CC7722', 'olive': '#808000',
         'orange': '#FF6600', 'orange-red': '#FF4500', 'orchid': '#DA70D6', 'peach': '#FFE5B4', 'pear': '#D1E231',
         'periwinkle': '#CCCCFF', 'persian blue': '#1C39BB', 'pink': '#FD6C9E', 'plum': '#8E4585',
         'prussian blue': '#003153', 'puce': '#CC8899', 'purple': '#800080', 'raspberry': '#E30B5C', 'red': '#FF0000',
         'red-violet': '#C71585', 'rose': '#FF007F', 'ruby': '#E0115F', 'salmon': '#FA8072', 'sangria': '#92000A',
         'sapphire': '#0F52BA', 'scarlet': '#FF2400', 'silver': '#C0C0C0', 'slate gray': '#708090',
         'spring bud': '#A7FC00', 'spring green': '#00FF7F', 'tan': '#D2B48C', 'taupe': '#483C32', 'teal': '#008080',
         'turquoise': '#40E0D0', 'ultramarine': '#3F00FF', 'violet': '#7F00FF', 'viridian': '#40826D',
         'white': '#FFFFFF', 'yellow': '#FFFF00'}
COLORS = {k.title(): v for k, v in COLOR.items()}
print(COLORS)

ls = [x.title() for x in word_tokenize(file) if x.title() in COLORS]
print(len(ls))

fig, ax = plt.subplots()
fig.set_size_inches((19.2, 10.8), forward=False)
fig.patch.set_facecolor('#191919')
plt.axis('off')

width = 0
height = 1
for i in range(0, len(ls)):
    plt.text(0 + width, height, ls[i], color=COLORS[ls[i]],
             fontproperties=prop, fontsize=8.5)
    width += 0.03
    if width > 0.95:
        width = 0
        height -= 0.030
plt.savefig('every_color.svg', format='svg', dpi=1200, bbox_inches="tight", facecolor='#191919')
plt.show()
