#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime
import os

df = pd.read_csv("../data/COVID-tokyo.csv", parse_dates=['date'])
# now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())
# now = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S}'
p = os.stat("../data/COVID-tokyo.csv")
now = f'{datetime.datetime.fromtimestamp(p.st_mtime):%Y-%m-%d %H:%M:%S}'

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['date'], df['confirmed'], color='C1', width=-1, align='edge')
# , edgecolor="black", linewidth=0.5)
ax.set_xlim(pd.to_datetime('2020-03-01'), df['date'].values[-1]) # + pd.to_timedelta(1, 'day'))
ax.legend(['Tokyo confirmed'], loc='upper left')

ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yticks([df['confirmed'].values[-1]])

# ax_pos = ax.get_position()
# fig.text(ax_pos.x1 + 0.01,
#          (df['confirmed'].values[-1] / ax.get_ylim()[1]) *  (ax_pos.y1 - ax_pos.y0) + ax_pos.y0,
#          df['confirmed'].values[-1], verticalalignment='center')

fig.savefig('../img/COVID-tokyo.svg', bbox_inches="tight")
fig.savefig('../img/COVID-tokyo.png', bbox_inches="tight")

#----

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

cmap = plt.get_cmap('tab20')
# col = ['C0', 'C0', 'C0', 'C0', 'C0', 'C1', 'C1']
col = [cmap(3), cmap(3), cmap(3), cmap(3), cmap(3), cmap(2), cmap(2)]
cols = [col[pd.Timestamp(i).dayofweek] for i in df['date'].values]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['date'], df['confirmed'], color=cols, width=1,
       align='edge',
       edgecolor="black", linewidth=0.5)
ax.set_xlim(pd.to_datetime('2020-12-01'), df['date'].values[-1] + pd.to_timedelta(1, 'day'))
# ax.legend(['Tokyo confirmed'], loc='upper left')

ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yticks([df['confirmed'].values[-1]])

# ax_pos = ax.get_position()
# fig.text(ax_pos.x1 + 0.01,
#          (df['confirmed'].values[-1] / ax.get_ylim()[1]) *  (ax_pos.y1 - ax_pos.y0) + ax_pos.y0,
#          df['confirmed'].values[-1], verticalalignment='center')

fig.savefig('../img/COVID-tokyo-a.svg', bbox_inches="tight")
fig.savefig('../img/COVID-tokyo-a.png', bbox_inches="tight")

#----

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.plot(df['date'], df['confirmed'], 'o-', color='C1')
ax.set_yscale('log')
ax.set_xlim(pd.to_datetime('2020-03-01'), df['date'].values[-1]) # + pd.to_timedelta(1, 'day'))
ax.legend(['Tokyo confirmed'], loc='upper left')
fig.savefig('../img/COVID-tokyo-log.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

def rt(i, interval):
    mean1 = df['confirmed'][i-6:i+1].mean()
    mean2 = df['confirmed'][i-6-interval:i+1-interval].mean()
    return (mean1 / mean2) ** (5/interval)

for interval in range(1, 8):
    a = [rt(i, interval) for i in range(300, df.shape[0])]
    plt.plot(df['date'][300:df.shape[0]], a, label=interval)
ax.set_xlim(pd.to_datetime('2020-12-01'), df['date'].values[-1] + pd.to_timedelta(1, 'day'))
plt.axhline(1, color='black', linewidth=1, zorder=-1)
plt.legend()
fig.savefig('../img/COVID-tokyo-rt.svg', bbox_inches="tight")
fig.savefig('../img/COVID-tokyo-rt.png', bbox_inches="tight")

#-----

exit()

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['date'], df['confirmed'].cumsum(), align='edge', label='Tokyo cumulative confirmed')
ax.set_xlim(pd.to_datetime('2020-03-01'), df['date'].values[-1] + pd.to_timedelta(1, 'day'))
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

exit()

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

cmap = plt.get_cmap('tab20')
# col = ['C0', 'C0', 'C0', 'C0', 'C0', 'C1', 'C1']
col = [cmap(3), cmap(3), cmap(3), cmap(3), cmap(3), cmap(2), cmap(2)]
cols = [col[pd.Timestamp(i).dayofweek] for i in df['date'].values]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df['date'], df['confirmed'], color=cols, width=1,
       align='edge',
       edgecolor="black", linewidth=0.5)
ax.set_xlim(pd.to_datetime('2020-12-01'), df['date'].values[-1] + pd.to_timedelta(1, 'day'))
# ax.legend(['Tokyo confirmed'], loc='upper left')

ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yticks([df['confirmed'].values[-1]])

# ax_pos = ax.get_position()
# fig.text(ax_pos.x1 + 0.01,
#          (df['confirmed'].values[-1] / ax.get_ylim()[1]) *  (ax_pos.y1 - ax_pos.y0) + ax_pos.y0,
#          df['confirmed'].values[-1], verticalalignment='center')

fig.savefig('../img/COVID-tokyo-a.svg', bbox_inches="tight")
