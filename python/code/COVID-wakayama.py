#! /usr/bin/env python3

# https://www.pref.wakayama.lg.jp/prefg/041200/d00203387.html

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-wakayama.csv", index_col='Date', parse_dates=['Date'])

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
dt = (df.index.to_series().diff() / pd.Timedelta(days=1))
ax.bar(df.index, df['Examined'].diff() / dt, width=-dt, align='edge', edgecolor="white")
ax.bar(df.index, df['Positive'].diff() / dt, width=-dt, align='edge', edgecolor="white")
ax.legend(['Negative', 'Positive'])
fig.savefig('../img/COVID-wakayama-dif.svg', bbox_inches="tight")
