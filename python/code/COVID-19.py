#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

df = pd.read_csv("../data/COVID-19.csv", index_col='Date', parse_dates=['Date'])
dfjp = pd.read_csv("../data/COVID-jp.csv", index_col='Date', parse_dates=['Date'])

cmap = plt.get_cmap("tab20")

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df.index, df['Global Confirmed'], color=cmap(3))
ax.bar(df.index, df['China Confirmed'], color=cmap(2))
ax.bar(df.index, df['Global Deaths'], color=cmap(6))
plt.legend(['Global Confirmed', 'China Confirmed', 'Global Deaths'])
plt.savefig('../img/COVID-19.svg', bbox_inches="tight")

plt.clf()
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.plot(df.index, df['Global Confirmed'], "s-", color=cmap(3))
ax.plot(df.index, df['China Confirmed'], "o-", color=cmap(2))
ax.plot(df.index, df['Global Deaths'], "s-", color=cmap(7))
ax.plot(df.index, df['China Deaths'], "o-", color=cmap(6))
ax.plot(dfjp.index, dfjp['Confirmed'], "x-", color=cmap(2))
ax.plot(dfjp.index, dfjp['Deaths'], "x-", color=cmap(6))
plt.yscale('log')
plt.grid()
plt.legend(['Global Confirmed', 'China Confirmed', 'Global Deaths', 'China Deaths', 'Japan Confirmed', 'Japan Deaths'])
plt.savefig('../img/COVID-19-log.svg', bbox_inches="tight")

plt.clf()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
dt = (df.index.to_series().diff() / pd.Timedelta(days=1))
gc = df['Global Confirmed'].diff()
gc[df.index == '2020-02-17'] = np.nan
ax.bar(df.index, gc / dt, width=-dt, align='edge', color=cmap(3), edgecolor="white")
cc = df['China Confirmed'].diff()
cc[df.index == '2020-02-17'] = np.nan
ax.bar(df.index, cc / dt, width=-dt, align='edge', color=cmap(2), edgecolor="white")
ax.bar(df.index, df['Global Deaths'].diff() / dt, width=-dt, align='edge', color=cmap(6), edgecolor="white")
plt.legend(['Global Confirmed', 'China Confirmed', 'Global Deaths'])
plt.savefig('../img/COVID-19-dif.svg', bbox_inches="tight")
