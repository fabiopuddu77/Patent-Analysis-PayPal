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


g = nx.from_pandas_edgelist(df_edges, source="source", target="target", edge_attr=["weight"],create_using=nx.Graph)

df = df_edges

clubs = list(df.source.unique())

people = list(df.target.unique())

dict(zip(clubs, clubs))

plt.figure(figsize=(12, 12))

# 1. Create the graph

# 2. Create a layout for our nodes
layout = nx.spring_layout(g,iterations=100)

# 3. Draw the parts we want
# Edges thin and grey
# People small and grey
# Clubs sized according to their number of connections
# Clubs blue
# Labels for clubs ONLY
# People who are highly connected are a highlighted color

# Go through every club name, ask the graph how many
# connections it has. Multiply that by 80 to get the circle size
club_size = [g.degree(club) * 90 for club in clubs]
nx.draw_networkx_nodes(g,
                       layout,
                       nodelist=clubs,
                       node_size=club_size, # a LIST of sizes, based on g.degree
                       node_color='lightblue')

# Draw EVERYONE
nx.draw_networkx_nodes(g, layout, nodelist=people, node_color='lightblue', node_size=300)

# Draw POPULAR PEOPLE
popular_people = [person for person in people if g.degree(person) > 10]
nx.draw_networkx_nodes(g, layout, nodelist=popular_people, node_color='#F4D03F', node_size=520)

nx.draw_networkx_edges(g, layout, width=1, edge_color="#D0D3D4")

node_labels = dict(zip(clubs,clubs))
nx.draw_networkx_labels(g, layout)

# 4. Turn off the axis because I know you don't want it
plt.axis('off')

plt.title("Class Patents")

# 5. Tell matplotlib to show it
plt.show()

