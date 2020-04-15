#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import re

Z2H = str.maketrans("　０１２３４５６７８９", " 0123456789")

tables = pd.read_html('http://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000071_00005.htm')
t = tables[0][1:-1].copy()
date = []
tests = []
positives = []
for i, x in t.iterrows():
    if str(x[0]) == 'nan':
        continue
    for j in range(4):
        x[j] = x[j].translate(Z2H)
    m = re.search(r'(\d+)月 *(\d+)日', x[0])
    if m:
        x[0] = pd.Timestamp(f'2020-{m[1]}-{m[2]}')
    for j in range(1, 4):
        x[j] = int(re.sub("件.*$", "", x[j]))
    date.append(x[0])
    tests.append(x[1])
    positives.append(x[2])

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(date, tests)
ax.bar(date, positives)
ax.legend(['Negative', 'Positive'])
# ax.set_yticks([0, 5, 10, 15, 20, 25])

fig.savefig('../img/COVID-mie.svg', bbox_inches="tight")
