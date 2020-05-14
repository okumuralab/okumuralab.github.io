#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import requests

url = 'https://www.worldometers.info/coronavirus/'
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"

# tables = pd.read_html(url) では User-Agent が "Python-urllib/3.7" になりエラー

r = requests.get(url, headers={'User-Agent': ua})
r.encoding = 'utf-8'
tables = pd.read_html(r.text)

df = tables[0][1:-1]

plt.figure(figsize=[6.4, 6.4])

plt.clf()
plt.plot(df['Tests/ 1M pop'], df['Deaths/1M pop'], 'o')
plt.plot(df['Tests/ 1M pop'][df['Country,Other'] == 'Japan'],
         df['Deaths/1M pop'][df['Country,Other'] == 'Japan'], 'o')
plt.xscale('log')
plt.yscale('log')
plt.axis('equal')
plt.xlabel('Tests/1M pop')
plt.ylabel('Deaths/1M pop')

for i, r in df.iterrows():
    if r['TotalCases'] >= 10000:
        plt.text(r['Tests/ 1M pop'], r['Deaths/1M pop'], r['Country,Other'],
                 horizontalalignment='left', verticalalignment='bottom')


