#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from dateutil.parser import parse
import datetime

df = pd.read_csv("https://dl.dropboxusercontent.com/s/6mztoeb6xf78g5w/COVID-19.csv")

t1 = [parse(str(x)) for x in df['発症日'] if str(x) != 'nan']
t2 = [parse(str(x)) for x in df['確定日'] if str(x) != 'nan']

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

b = np.arange(min(t1), max(t2) + datetime.timedelta(days=2), datetime.timedelta(days=1))

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.hist(t1, bins=b, edgecolor="black", alpha=0.5) # color=cmap(1), 
ax.hist(t2, bins=b, edgecolor="black", alpha=0.5) # color=cmap(3), 
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312a.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

h1, h2 = np.histogram(t1, bins=b)
ax.plot(h2[:-1], h1, 'o-')
h1, h2 = np.histogram(t2, bins=b)
ax.plot(h2[:-1], h1, 'o-')
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312b.svg', bbox_inches="tight")

#-----

dt = [(parse(x['確定日']) - parse(x['発症日'])).days
      for i, x in df.iterrows() if str(x['発症日']) != 'nan']

ax.clear()
ax.hist(dt, bins=range(min(dt), max(dt)+2), color="lightgray", edgecolor="black")
ax.legend(['確定日-発症日 (confirmed - onset)'])
ax.text(0.98, 0.87, 'median: ' + str(np.median(dt)),
        horizontalalignment='right', transform=ax.transAxes)

fig.savefig('../img/200312c.svg', bbox_inches="tight")

#-----

# t = [parse(x['確定日']) for i, x in df.iterrows() if str(x['発症日']) != 'nan']
# 
# ax.clear()
# ax.plot(t, dt, 'ko', markersize=5, alpha=0.3)
# 
# fig.savefig('../img/200312f.svg', bbox_inches="tight")

#-----

ax.clear()
w2 = [pd.Timestamp(t).dayofweek for t in t2]
h1, h2 = np.histogram(w2, range(0,8))
ax.bar(['月','火','水','木','金','土','日'], h1, color="lightgray", edgecolor="black")
ax.set_xlabel('確定日')

fig.savefig('../img/200312d.svg', bbox_inches="tight")

#-----

ax.clear()
w1 = [pd.Timestamp(t).dayofweek for t in t1]
h1, h2 = np.histogram(w1, range(0,8))
ax.bar(['月','火','水','木','金','土','日'], h1, color="lightgray", edgecolor="black")
ax.set_xlabel('発症日')

fig.savefig('../img/200312e.svg', bbox_inches="tight")
