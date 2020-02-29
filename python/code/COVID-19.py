#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

df = pd.read_csv("../data/COVID-19.csv", index_col='Date', parse_dates=['Date'])

cmap = plt.get_cmap("tab20")

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df.index, df['Global Confirmed'], color=cmap(3))
ax.bar(df.index, df['Global Deaths'], color=cmap(6))
plt.legend(['Confirmed', 'Deaths'])
plt.savefig('../img/COVID-19.svg', bbox_inches="tight")

plt.clf()
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.plot(df.index, df['Global Confirmed'], "o-", color=cmap(2))
ax.plot(df.index, df['Global Deaths'], "s-", color=cmap(6))
plt.yscale('log')
plt.legend(['Confirmed', 'Deaths'])
plt.savefig('../img/COVID-19-log.svg', bbox_inches="tight")

plt.clf()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
dt = (df.index.to_series().diff() / pd.Timedelta(days=1))
c = df['Global Confirmed'].diff()
c[df.index == '2020-02-17'] = np.nan
ax.bar(df.index, c / dt, width=-dt, align='edge', color=cmap(3), edgecolor="white")
ax.bar(df.index, df['Global Deaths'].diff() / dt, width=-dt, align='edge', color=cmap(6), edgecolor="white")
plt.legend(['Confirmed', 'Deaths'])
plt.savefig('../img/COVID-19-dif.svg', bbox_inches="tight")
