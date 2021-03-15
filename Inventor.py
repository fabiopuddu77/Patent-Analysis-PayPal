import string

import matplotlib
import nltk
import pandas as pd
import network2 as nx
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import csv

import itertools

df = pd.read_csv("./Abstract/paypal_dv.csv", error_bad_lines=False, sep=';')
df_cities = pd.read_csv("./Abstract/uscities.csv", error_bad_lines=False, sep=',')

lista_inv = [i.replace("|",",").replace('.','').replace(' ','') for i in df["Inventor - w/address"]]

parole = ",".join(lista_inv).split(',')

lista_cit = [i for i in df_cities['city']]
lista_county = [i for i in df_cities['county_name']]

#diz = [(city,county,parole.count(city)) for city in parole if city in lista_cit if county in df_cities['county_name']]

#print(diz.keys())

# df = pd.DataFrame(diz.items(), columns=['City', 'Frequency'])
#
#
# df.to_csv('cities_freq.csv', index=False)