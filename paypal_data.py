import matplotlib
import seaborn as sns
import nltk
import math


matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pandas as pd


#df = pd.read_csv("./Abstract/paypal_dv.csv", error_bad_lines=False, sep=';')
df3 = pd.read_csv("./Abstract/AppDate15.csv", error_bad_lines=False, sep=';')


# class Dataframe():
#
#     def __init__(self, df, nome):
#
#         self.df = df
#         self.nome = self.df["DWPIManualCodes"]
#         print(self.nome)
#
#
#     def lista_col(self):
#         a =  [i for i in self.nome if str(i) != "nan"]
#         return (",").join(a).replace(" ","").split(",")
#
#
#
#     def freq_dist(self):
#         # lista = nltk.Text(self.lista_col())
#         return nltk.FreqDist([w for w in nltk.Text(self.lista_col())])
#
#     def parole(self):
#         return [i for i in self.freq_dist()]

# def get_edges(data, column):
#   series = data[column].dropna().apply(lambda x: x.split(", "))
#   cross = series.apply(lambda x: [i for i in combinations(x, 2)])
#   lists = [item for sublist in cross for item in sublist]
#   source = [i[0] for i in lists]
#   target = [i[1] for i in lists]
#   edges = pd.DataFrame({"source": source, "target": target})
#   edges["weight"] = 1
#   return edges.groupby(by=["source", "target"], as_index=False)["weight"].sum()
#
#
# df_edges = get_edges(data=brevetti_y[brevetti_y["Publication Year"]==2015], column="CPC Class")
#
# G = nx.from_pandas_edgelist(df_edges, source="source", target="target", edge_attr=["weight"],create_using=nx.Graph)
# pos = nx.spring_layout(G, k=2.5)

#
# class Frequenza():
#     def __init__(self, lista, stato, anno):
#         self.lista = lista
#         self.stato = stato
#         self.anno = anno
#
#
#     def numeri(self):
#         return [(i,self.lista.count(i)) for i in self.lista]
#
#     def stati(self):
#         pass
#
#
#     def finale(self):
#         l = []
#         for i in self.numeri():
#             if i not in l:
#                 l.append(i)
#         return sorted(l)
#
#     def conteggio(self):
#         l = [(i,j[0]) for i in lista_anni for j in lista_state_pub]
#         return [i for i in l if i[1] == self.stato and i[0] == self.anno]
#
#
#
# f1 = Frequenza(lista_anni,"US",2020)
#
#
# print((f1.conteggio()))







# print(df['Publication Year'])
# plt.figure(figsize=(10,8))
# sns.countplot(df["Publication Year"], color="blue")
# plt.tight_layout()
# plt.show()

# df['Publication Year'].value_counts().sort_index().plot.bar()
# plt.show()

# sns.distplot(df['Publication Year'], bins=10, kde=True)
# plt.show()

# with sns.axes_style('white'):
#     g = sns.factorplot("Publication Year", data=df, aspect=2,
#                        kind="count", color='steelblue')
#     g.set_xticklabels(step=5)
#     plt.show()

# with sns.axes_style('white'):
#     g = sns.factorplot("Publication Year", aspect=4.0, kind='count',
#                        hue='Publication Country Code', order=range(2000, 2021))
#     g.set_ylabels('Number of Class Discovered')
#     plt.show()

if __name__ == "__main__":

    #df = pd.read_csv("./Abstract/paypal_dv.csv", error_bad_lines=False, sep=';')

    #D = Dataframe(df3,"DWPIManualCodes")


    #df2 = pd.DataFrame(D.lista_col(),columns=["class"])

    #print(df2)
    plt.figure(figsize=(10, 8))
    sns.countplot(sorted(df3["ApplicationDate"]), color="darkred")
    plt.tight_layout()
    plt.show()



