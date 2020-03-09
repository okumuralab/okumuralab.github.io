#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-jp.csv", index_col='Date', parse_dates=['Date'])

cmap = plt.get_cmap("tab20")
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.bar(df.index, df['Confirmed'], color=cmap(3))
ax.bar(df.index, df['Deaths'], color=cmap(6))
ax.legend(['Confirmed (Japan)', 'Deaths (Japan)'])
fig.savefig('../img/COVID-jp.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
dt = (df.index.to_series().diff() / pd.Timedelta(days=1))
ax.bar(df.index, df['Confirmed'].diff() / dt, width=-dt, align='edge', color=cmap(3), edgecolor="white")
ax.bar(df.index, df['Deaths'].diff() / dt, width=-dt, align='edge', color=cmap(6), edgecolor="white")
ax.legend(['Confirmed', 'Deaths'])
fig.savefig('../img/COVID-jp-dif.svg', bbox_inches="tight")
