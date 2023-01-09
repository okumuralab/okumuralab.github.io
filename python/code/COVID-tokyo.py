#! /usr/local/bin/python3

import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-tokyo.csv", parse_dates=['date'])
p = os.stat("../data/COVID-tokyo.csv")
now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(p.st_mtime))

t = df['date'].values
x = df['confirmed'].values

DAY = pd.to_timedelta(1, 'day')
t1 = pd.to_datetime('2022-06-01')
t2 = t[-1] + DAY

fig, ax = plt.subplots()
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.bar(t, x, color='C1', width=-DAY, align='edge')
ax.set_xlim(pd.to_datetime('2020-03-01'), t[-1])
ax.legend(['Tokyo confirmed'], loc='upper left')

ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yticks([x[-1]])

fig.savefig('../img/COVID-tokyo.svg', bbox_inches="tight")

#----

ax.clear()

cmap = plt.get_cmap('tab20')
col = [cmap(3), cmap(3), cmap(3), cmap(3), cmap(3), cmap(2), cmap(2)]
cols = np.array([col[pd.Timestamp(i).dayofweek] for i in t])

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.bar(t[t >= t1], x[t >= t1], color=cols[t >= t1], width=DAY,
       align='edge', edgecolor="black", linewidth=0.5)
ax.set_xlim(t1, t2)

ax2.set_ylim(ax.get_ylim())

fig.savefig('../img/COVID-tokyo-a.svg', bbox_inches="tight")
fig.savefig('../img/COVID-tokyo-a.png', bbox_inches="tight")

#----

ax.clear()
ax2.set_yticks([])

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.plot(t, x, 'o-', color='C1')
ax.set_yscale('log')
ax.set_xlim(pd.to_datetime('2020-03-01'), t[-1])
ax.legend(['Tokyo confirmed'], loc='upper left')

fig.savefig('../img/COVID-tokyo-log.svg', bbox_inches="tight")

#-----

ax.clear()

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

def rt(i, interval):
    if i - 6 - interval < 0:
        return np.nan
    mean1 = x[i-6:i+1].mean()
    mean2 = x[i-6-interval:i+1-interval].mean()
    if mean2 == 0:
        return np.nan
    return (mean1 / mean2) ** (5/interval)

for interval in range(1, 8):
    a = np.array([rt(i, interval) for i in range(len(t))])
    ax.plot(t[t >= t1], a[t >= t1], label=interval)

ax.axhline(1, color='black', linewidth=1, zorder=-1)
ax.set_xlim(t1, t2)
ax.legend()

fig.savefig('../img/COVID-tokyo-rt.svg', bbox_inches="tight")
fig.savefig('../img/COVID-tokyo-rt.png', bbox_inches="tight")
