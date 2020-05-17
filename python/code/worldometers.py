#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

url = 'https://www.worldometers.info/coronavirus/'
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"

# tables = pd.read_html(url) では User-Agent が "Python-urllib/3.7" になりエラー

now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())
r = requests.get(url, headers={'User-Agent': ua})
r.encoding = 'utf-8'
tables = pd.read_html(r.text)

df = tables[0][1:-1]

plt.figure(figsize=[6.4, 6.4])

c = 'Country,Other'
japan = df[c] == 'Japan'
usa = df[c] == 'USA'
minpop = 50000000

#-----

x = 'Tot Cases/1M pop'
y = 'Tests/ 1M pop'

plt.clf()
plt.plot(df[x], df[y], 'o', alpha=0.5)
plt.plot(df[x][japan], df[y][japan], 'o', color='C1')
plt.plot(df[x][usa], df[y][usa], 'o', color='C3')
plt.xscale('log')
plt.yscale('log')
plt.axis('equal')
plt.xlabel(x)
plt.ylabel(y)

for i, r in df.iterrows():
    if r['Population'] >= minpop:
        plt.text(r[x], r[y], r[c],
                 horizontalalignment='left', verticalalignment='bottom')

xj = np.array([min(df[x]), max(df[x])])
k = (df[y][japan] / df[x][japan]).values[0]
yj = k * xj

plt.autoscale(False)
plt.plot(xj, yj, color='lightgray', label=f"Tests / Cases = {k:.1f} (Japan)")
plt.legend()
plt.figtext(0.9, 0.9, 'generated: ' + now, horizontalalignment='right')
plt.savefig('../img/worldometers1.svg', bbox_inches="tight")

#-----

x = 'Deaths/1M pop'
y = 'Tests/ 1M pop'

plt.clf()
plt.plot(df[x], df[y], 'o', alpha=0.5)
plt.plot(df[x][japan], df[y][japan], 'o', color='C1')
plt.plot(df[x][usa], df[y][usa], 'o', color='C3')
plt.xscale('log')
plt.yscale('log')
plt.axis('equal')
plt.xlabel(x)
plt.ylabel(y)

for i, r in df.iterrows():
    if r['Population'] >= minpop:
        plt.text(r[x], r[y], r[c],
                 horizontalalignment='left', verticalalignment='bottom')

xj = np.array([min(df[x]), max(df[x])])
k = (df[y][japan] / df[x][japan]).values[0]
yj = k * xj

plt.autoscale(False)
plt.plot(xj, yj, color='lightgray', label=f"Tests / Deaths = {k:.0f} (Japan)")
plt.legend()
plt.figtext(0.9, 0.9, 'generated: ' + now, horizontalalignment='right')
plt.savefig('../img/worldometers2.svg', bbox_inches="tight")

exit()

#-----

x = 'Tests/ 1M pop'
y = 'Deaths/1M pop'

plt.clf()
plt.plot(df[x], df[y], 'o')
plt.plot(df[x][japan], df[y][japan], 'o')
plt.plot(df[x][usa], df[y][usa], 'o')
plt.xscale('log')
plt.yscale('log')
plt.axis('equal')
plt.xlabel(x)
plt.ylabel(y)

for i, r in df.iterrows():
    if r['Population'] >= minpop:
        plt.text(r[x], r[y], r[c],
                 horizontalalignment='left', verticalalignment='bottom')

xj = np.array([min(df[x]), max(df[x])])
k = (df[y][japan] / df[x][japan]).values[0]
yj = k * xj

plt.autoscale(False)
plt.plot(xj, yj, color='lightgray', label=f"Deaths / Tests = {k:.4f} (Japan)")
plt.legend(loc='upper left')
