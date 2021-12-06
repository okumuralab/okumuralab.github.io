#! /usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import time

def readcsv(url):
    try:
        df = pd.read_csv(url, parse_dates=['日付'])
        print('utf-8:', url)
    except UnicodeDecodeError:
        df = pd.read_csv(url, parse_dates=['日付'], encoding='cp932')
        print('cp932:', url)
    return df

now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

# PCR検査陽性者数
# df1 = readcsv("https://www.mhlw.go.jp/content/pcr_positive_daily.csv")
df1 = pd.read_csv("https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv", parse_dates=['Date'])
# df1 = df1[df1.Prefecture == "ALL"]

# PCR 検査実施件数(単日)
df2 = readcsv("https://www.mhlw.go.jp/content/pcr_tested_daily.csv")

# 死亡者数
# df5 = readcsv("https://www.mhlw.go.jp/content/death_total.csv")
df5 = pd.read_csv("https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv", parse_dates=['Date'])
# df5 = df5[df5.Prefecture == "ALL"]

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df2['日付'], df2['PCR 検査実施件数(単日)'], width=1)
# ax.bar(df1['Date'], df1['Newly confirmed cases'], width=1)
ax.bar(df1['Date'], df1['ALL'], width=1)
ax.legend(['Negative', 'Positive'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen1.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
# ax.bar(df1['Date'], df1['Newly confirmed cases'], width=1, color='C1')
ax.bar(df1['Date'], df1['ALL'], width=1, color='C1')
# ax.bar(df5['Date'], df5['Deaths(Cumulative)'].diff(), width=1, color='C3')
ax.bar(df5['Date'], df5['ALL'].diff(), width=1, color='C3')
ax.legend(['Positive', 'Deaths'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen2.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
# ax.bar(df5['Date'], df5['Deaths(Cumulative)'].diff(), width=1, color='C3')
ax.bar(df5['Date'], df5['ALL'].diff(), width=1, color='C3')
ax.legend(['Deaths'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen3.svg', bbox_inches="tight")
