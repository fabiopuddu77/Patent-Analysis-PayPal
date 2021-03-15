
import nltk
import PIL
from PIL import Image
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords, CategorizedPlaintextCorpusReader
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd
from wordcloud import WordCloud

class Document():

    def __init__(self, dir, doc):
        self.doc = doc
        self.dir = dir
        self.eng_stopw = stopwords.words('english')


        text_corpus = CategorizedPlaintextCorpusReader(
            './%s/' % self.dir,
            r'.*\.txt',  # leggo solamente i file che terminato con .csv
            cat_pattern=r'(\w+)/*',  # prendi tutto quello che c'è dopo la directory
            encoding='latin-1'
        )

        self.text = nltk.Text(text_corpus.words(self.doc))

    def freq_dist(self):
        return nltk.FreqDist([w for w in self.text if len(w) >= 2])

    def parole(self):
        return [(i) for i in self.freq_dist().most_common()]

    def tokenize(self):
        return ([w for w in self.text if len(w) >= 4 and w not in self.eng_stopw])

    def wordcloud(self,stopword,mask_k):

        list = (" ").join(self.tokenize())
        wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white",stopwords=stopword,
                              collocations=False,
                              repeat=False, contour_width=3, contour_color='firebrick',mask=mask_k).generate(list)
        plt.figure(figsize=[20,10])
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        return


if __name__ == "__main__":
    file3 = Document("./Abstract", "Stati2015.txt")


    print(file3.parole())
    ###### WORDCLOUD ######
    paypal_mask = np.array(Image.open("./Abstract/paypal.png"))
    def transform_format(val):
        if val.any() == 0:
            return 255
        else:
            return val

    transformed_pp_mask = np.ndarray((paypal_mask.shape[0], paypal_mask.shape[1]), np.int32)

    for i in range(len(paypal_mask)):
         transformed_pp_mask = list(map(transform_format, paypal_mask[i]))


    stopword = set()
    stopword.update(["system"])

    file2 = Document("./Abstract","pp_tit_dwpi.csv")
    print("WordCloud",file2.wordcloud(stopword,paypal_mask))