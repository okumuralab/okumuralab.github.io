#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import time

df = pd.read_csv("../data/COVID-tokyo.csv", parse_dates=['date'])
now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

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

exit()

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
# ax.plot(df['date'], df['confirmed'].cumsum(), label='Tokyo cumulative confirmed')
c = df['confirmed'].cumsum()
ax.plot(df['date'][c >= 100], c[c >= 100], 'o-', label='Tokyo cumulative confirmed')
ax.set_yscale('log')
ax.legend(loc='upper left')

ax.clear()
w = [[pd.Timestamp(t).dayofweek] * c for t, c in zip(df['date'], df['confirmed'])]
w = sum(w, [])
h1, h2 = np.histogram(w, range(0,8))
ax.bar(['月','火','水','木','金','土','日'], h1, color="lightgray", edgecolor="black")
ax.set_xlabel('確定日')
