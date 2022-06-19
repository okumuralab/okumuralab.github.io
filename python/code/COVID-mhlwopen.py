#! /usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import time

def readcsv(url):
    try:
        df = pd.read_csv(url, parse_dates=[0], thousands=",")
        print('utf-8:', url)
    except UnicodeDecodeError:
        df = pd.read_csv(url, parse_dates=[0], encoding='cp932')
        print('cp932:', url)
    return df

now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

# PCR検査実施人数
df1 = readcsv("https://www.mhlw.go.jp/content/pcr_tested_daily.csv")

# 新規陽性者数の推移（日別）
df2 = readcsv("https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv")

# 死亡者数（累積）
df3 = readcsv("https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv")

fig, ax = plt.subplots()
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df1.iloc[:,0], df1.iloc[:,1], width=1)
ax.bar(df2['Date'], df2['ALL'], width=1)
ax.legend(['Negative', 'Positive'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen1.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df2['Date'], df2['ALL'], width=1, color='C1')
ax.bar(df3['Date'], df3['ALL'].diff(), width=1, color='C3')
ax.legend(['Positive', 'Deaths'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen2.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df3['Date'], df3['ALL'].diff(), width=1, color='C3')
ax.legend(['Deaths'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen3.svg', bbox_inches="tight")
