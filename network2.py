
import matplotlib
import nltk
import pandas as pd
import networkx as nx
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import itertools


df = pd.read_csv("./Abstract/paypal_dv.csv", error_bad_lines=False, sep=';')

def get_edges(data, column):
  series = data[column].dropna().apply(lambda x: x.split(", "))

  cross = series.apply(lambda x: list(itertools.combinations(x, 2)))

  lists = [item for sublist in cross for item in sublist]

  source = [i[0] for i in lists]
  target = [i[1] for i in lists]
  edges = pd.DataFrame({"source": source, "target": target})
  edges["weight"] = 1
  return edges.groupby(by=["source", "target"], as_index=False)["weight"].sum()


df_edges = get_edges(data=df, column="CPC Class - DWPI")

G = nx.from_pandas_edgelist(df_edges, source="source", target="target", edge_attr=["weight"],create_using=nx.Graph)

pos = nx.spring_layout(G)  # positions for all nodes

node_color = [G.degree(v) for v in G]
node_size = [0.0005 * nx.get_node_attributes(G, 'target')[v] for v in G]
edge_width = [0.0015 * G[u][v]['weight'] for u, v in G.edges()]

nx.draw_networkx(G, node_size=node_size,
                 node_color=node_color, alpha=0.7,
                 with_labels=True, width=edge_width,
                 edge_color='.4', cmap=plt.cm.Blues)

plt.axis('off')
plt.tight_layout()
plt.show()