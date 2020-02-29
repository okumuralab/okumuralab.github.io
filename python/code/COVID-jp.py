#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-jp.csv", index_col='Date', parse_dates=['Date'])

cmap = plt.get_cmap("tab20")

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df.index, df['Confirmed'], color=cmap(3))
ax.bar(df.index, df['Deaths'], color=cmap(6))
plt.legend(['Confirmed (Japan)', 'Deaths (Japan)'])
plt.savefig('../img/COVID-jp.svg', bbox_inches="tight")
