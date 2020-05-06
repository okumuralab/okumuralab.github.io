#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import requests
import re

r = requests.get('https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000066_00002.htm')
r.encoding = 'utf-8'
a = re.findall(' href="(.*?\.csv)"', r.text)
url = 'https://www.pref.mie.lg.jp' + a[1]

df = pd.read_csv(url, encoding='cp932', parse_dates=['日付'])

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['日付'], df['検査件数'])
ax.bar(df['日付'], df['陽性'])
ax.legend(['Negative', 'Positive'])

fig.savefig('../img/COVID-mie.svg', bbox_inches="tight")
