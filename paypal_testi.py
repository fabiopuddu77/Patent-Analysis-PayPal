import numpy as np
import PIL
from PIL import Image
#import pandas as pd

import nltk

# import matplotlib
# matplotlib.use('TkAgg')
# from matplotlib import pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords, CategorizedPlaintextCorpusReader
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from wordcloud import WordCloud

# doc1 = (
#     """Era un oggetto troppo grande per chiamarlo spada. Troppo spesso, troppo pesante e grezzo.
#     Non era altro che un enorme blocco di ferro ferro ferro ferro ferro ferro ferro ferroferro ferro ferro ferro ferro ferro ferro ferroferro ferro ferro ferro ferro ferro ferro ferroferro ferro ferro ferro ferro ferro ferro ferro.
#     """
# )

# max valore più grande nella lista, ogni valore è il conteggio di un token

# class Document(object):
#
#     def __init__(self, text):
#         self.text = text
#         self.tokens = self.tokenize()
#         self.max_freq = max([self.tokens.count(t) for t in self.tokens])
#
#     def tokenize(self):
#         return [w.lower() for w in re.split(r'\W+', self.text) if w]
#
#     def tf(self, token):
#         return self.tokens.count(token) / self.max_freq

#df = pd.read_csv("./Abstract/paypal_dv.csv", error_bad_lines=False, sep=';')


class Document():

    def __init__(self, dir, doc):
        self.doc = doc
        self.dir = dir
        self.eng_stopw = stopwords.words('english')


        text_corpus = CategorizedPlaintextCorpusReader(
            './%s/' % self.dir,
            r'.*\.csv',  # leggo solamente i file che terminato con .csv
            cat_pattern=r'(\w+)/*',  # prendi tutto quello che c'è dopo la directory
            encoding='latin-1'
        )

        self.text = nltk.Text(text_corpus.words(self.doc))

    def freq_dist(self):
        return nltk.FreqDist([w for w in self.text if len(w) >= 4 and w not in self.eng_stopw])

    def parole(self):
        return [(i) for i in self.freq_dist().most_common(500)]

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


#
# df = pd.read_excel("/Users/utente/PycharmProjects/WAAT-2020_new/Abstract/Abstract.xlsx",skiprows=[0])
# print(df)
#
# df['Abstract - DWPI Detailed Description']
# testi = [testi for testi in df['Abstract']]
# stop_words = set(stopwords.words('english'))
#
# tokens = [word_tokenize(text) for text in testi if type(text)==str ]
#
#
# tokens_tot = [tokens.append(token) for lista in tokens for token in lista]
#
# tokens_tot

# with open("./Abstract/Abstract.csv", "r") as f:
#     read = f.readlines()



if __name__ == "__main__":

    ###### WORDCLOUD ######
    # paypal_mask = np.array(Image.open("./Abstract/paypal.png"))
    # def transform_format(val):
    #     if val.any() == 0:
    #         return 255
    #     else:
    #         return val
    #
    # transformed_pp_mask = np.ndarray((paypal_mask.shape[0], paypal_mask.shape[1]), np.int32)
    #
    # for i in range(len(paypal_mask)):
    #      transformed_pp_mask = list(map(transform_format, paypal_mask[i]))


    #
    # stopword = set()
    # stopword.update(["system"])

    #file2 = Document("./Abstract","pp_tit_dwpi.csv")
    # print("WordCloud",file2.wordcloud(stopword,paypal_mask))

    file3 = Document("", "pp_man_c.csv")

    # print(file.wordcloud())
    print(file3.parole())






    #file_dv = Document("./Abstract","paypal_dv.csv")
