#! /usr/local/bin/python3

import os
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
# import requests
# import re
import time

# r = requests.get('https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000066_00002.htm')
# r.encoding = 'utf-8'
# a = re.findall(' href="(.*?\.csv)"', r.text)
# url = 'https://www.pref.mie.lg.jp' + a[1]

# url = 'https://www.pref.mie.lg.jp/common/content/000896967.csv'
URL = "https://www.pref.mie.lg.jp/common/content/000948322.csv"
os.system("wget -N " + URL)
p = os.stat("000948322.csv")
now = f'{datetime.datetime.fromtimestamp(p.st_mtime):%Y-%m-%d %H:%M:%S}'
df = pd.read_csv("000948322.csv", encoding='cp932', parse_dates=['日付'])

# df = pd.read_csv(url, encoding='cp932', parse_dates=['日付'])
# now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['日付'], df['検査件数'], width=1)
ax.bar(df['日付'], df['陽性'], width=1)
ax.legend(['Negative', 'Positive'])

fig.savefig('../img/COVID-mie.svg', bbox_inches="tight")
