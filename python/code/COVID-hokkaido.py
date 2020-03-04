#! /usr/bin/env python3

# http://www.pref.hokkaido.lg.jp/hf/kth/kak/singatakoronahaien.htm 対策本部会議

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-hokkaido.csv", index_col='Date', parse_dates=['Date'])

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
