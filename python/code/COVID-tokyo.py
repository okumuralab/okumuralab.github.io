#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-tokyo.csv", parse_dates=['date'])

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['date'], df['confirmed'], color='C1', width=1, align='edge', edgecolor="black")
ax.legend(['Tokyo confirmed'], loc='upper left')
fig.savefig('../img/COVID-tokyo.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['date'], df['confirmed'].cumsum(), align='edge', label='Tokyo cumulative confirmed')
mx = df['confirmed'].cumsum().values[-1]
ax.axhline(mx, color='gray', linestyle='--', zorder=-1)
ax.axhline(mx/2, color='gray', linestyle='--', zorder=-1)
ax.legend(loc='upper left')
fig.savefig('../img/COVID-tokyo-cum.svg', bbox_inches="tight")

