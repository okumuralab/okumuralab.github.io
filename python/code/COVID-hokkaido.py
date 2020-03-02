#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-hokkaido.csv", index_col='Date', parse_dates=['Date'])

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df.index, df['Examined'])
ax.bar(df.index, df['Positive'])
plt.legend(['Negative', 'Positive'])
plt.savefig('../img/COVID-hokkaido.svg', bbox_inches="tight")

plt.clf()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
dt = (df.index.to_series().diff() / pd.Timedelta(days=1))
ax.bar(df.index, df['Examined'].diff() / dt, width=-dt, align='edge', edgecolor="white")
ax.bar(df.index, df['Positive'].diff() / dt, width=-dt, align='edge', edgecolor="white")
plt.legend(['Negative', 'Positive'])
plt.savefig('../img/COVID-hokkaido-dif.svg', bbox_inches="tight")
