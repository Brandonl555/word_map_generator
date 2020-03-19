from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import csv
import requests

us_ = []
non_us = []

#inverted water droplet: http://www.clker.com/cliparts/6/6/G/O/J/S/water-md.png
#house:http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png

mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))


def fill_(words_, ls):
    s = words_.split(",")
    for word__ in s:
        ls.append(word__)


def read_mydata(path):
    flag = False
    with open(path, newline='') as df:
        reader = csv.reader(df, delimiter=',')
        for row in reader:
            if not flag:
                flag = True
                continue

            words = row[3]
            if "US" in row[1]:
                fill_(words, us_)
            else:
                fill_(words, non_us)


def generate_wordcloud(words, mask_):
    word_cloud = WordCloud(width=256, height=256, background_color='white', stopwords=STOPWORDS, mask=mask_).generate(words)
    plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()


read_mydata('data/final_project_data.csv')

us_ = str(us_).strip('[]')
non_us = str(non_us).strip('[]')

generate_wordcloud(us_, mask)
generate_wordcloud(non_us, mask)



