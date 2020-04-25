#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv("https://dl.dropboxusercontent.com/s/6mztoeb6xf78g5w/COVID-19.csv",
                 parse_dates=['確定日', '発症日'])

b = np.arange(min(min(df['確定日']), min(df['発症日'])),
              max(max(df['確定日']), max(df['発症日'])) + datetime.timedelta(days=2),
              datetime.timedelta(days=1))

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.hist(df['発症日'], bins=b, edgecolor="black", alpha=0.5)
ax.hist(df['確定日'], bins=b, edgecolor="black", alpha=0.5)
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312a.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

h1, h2 = np.histogram(df['発症日'], bins=b)
ax.plot(h2[:-1], h1, 'o-')
h1, h2 = np.histogram(df['確定日'], bins=b)
ax.plot(h2[:-1], h1, 'o-')
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312b.svg', bbox_inches="tight")

#-----

dt = (df['確定日'] - df['発症日']).dt.days

ax.clear()
ax.hist(dt, bins=np.arange(min(dt), max(dt)+2), color="lightgray", edgecolor="black")
ax.legend(['確定日-発症日 (confirmed - onset)'])
ax.text(0.98, 0.87, 'median: ' + str(np.median(dt.dropna())),
        horizontalalignment='right', transform=ax.transAxes)

fig.savefig('../img/200312c.svg', bbox_inches="tight")

#-----

h = [np.nanmedian(dt[df['確定日'] == i]) for i in b]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.plot(df['確定日'], dt, 'ko', markersize=5, alpha=0.1)
ax.plot(b, h, color='C1')
ax.set_xlabel('確定日 (confirmed)')
ax.set_ylabel('確定日-発症日 (confirmed - onset)')

fig.savefig('../img/200312f.svg', bbox_inches="tight")

#-----

ax.clear()
w2 = [t.dayofweek for t in df['確定日']]
h1, h2 = np.histogram(w2, range(0,8))
ax.bar(['月','火','水','木','金','土','日'], h1, color="lightgray", edgecolor="black")
ax.set_xlabel('確定日')

fig.savefig('../img/200312d.svg', bbox_inches="tight")

#-----

ax.clear()
w1 = [t.dayofweek for t in df['発症日']]
h1, h2 = np.histogram(w1, range(0,8))
ax.bar(['月','火','水','木','金','土','日'], h1, color="lightgray", edgecolor="black")
ax.set_xlabel('発症日')

fig.savefig('../img/200312e.svg', bbox_inches="tight")
