#! /usr/local/bin/python3

# https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068
# wget -N https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv

import os
import subprocess
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

URL = "https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv"

r = subprocess.run(["wget", "-N", URL],
                   capture_output=True, text=True,
                   env={"PATH": "/usr/local/bin:/usr/bin",
                        "LANG": "en"})
if not " saved " in r.stderr:
    print("COVID-tokyo2.py: not modified.")  # 304 Not Modified
    exit()

p = os.stat("130001_tokyo_covid19_patients.csv")
now = f'{datetime.datetime.fromtimestamp(p.st_mtime):%Y-%m-%d %H:%M:%S}'

df = pd.read_csv("130001_tokyo_covid19_patients.csv",
                 parse_dates=['公表_年月日', '発症_年月日', '確定_年月日'],
                 na_values=['-', '―', '－', ' ', '不明', '不明性'],
                 low_memory=False)

# for c in df.columns:
#     print()
#     print(c)
#     print(df[c].value_counts())

# df.isna().sum()

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

fig, ax = plt.subplots()
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

b = np.arange(np.min(df['公表_年月日']),
              np.max(df['公表_年月日']) + np.timedelta64(2, "D"),
              np.timedelta64(1, "D"))

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.hist(df['公表_年月日'].values, bins=b, alpha=0.5)
ax.hist(df['発症_年月日'].values, bins=b, alpha=0.5)
ax.set_xlim(np.datetime64('2020-03-01'), b[-1])
ax.legend(['公表日', '発症日'])
fig.savefig('../img/COVID-tokyo2.svg', bbox_inches="tight")

onsets, _ = np.histogram(df['発症_年月日'].values, bins=b)
cmap = plt.get_cmap('tab20')
col = [cmap(3), cmap(3), cmap(3), cmap(3), cmap(3), cmap(2), cmap(2)]
cols = [col[pd.Timestamp(i).dayofweek] for i in b[:-1]]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.hist(df['公表_年月日'].values, bins=b, alpha=0.5)
# ax.hist(df['発症_年月日'].values, bins=b, alpha=0.5, edgecolor="black", linewidth=0.5)
ax.bar(b[:-1], onsets, alpha=0.5, width=0.99, color=cols, align='edge',
       edgecolor="black", linewidth=0.5)
ax.set_xlim(np.datetime64('2021-01-01'), b[-1])
ax.legend(['公表日', '発症日'])
fig.savefig('../img/COVID-tokyo2f.svg', bbox_inches="tight")

ax.clear()
t = (df['公表_年月日'] - df['発症_年月日']).dt.days
ax.hist(t, range(int(np.nanmin(t)), int(np.nanmax(t)) + 2),
         color="lightgray", edgecolor="black")
ax.set_xlim(0, 20)
ax.set_xticks(range(0, 25, 5))
ax.legend(['公表日-発症日 median=' + str(np.nanmedian(t))])
fig.savefig('../img/COVID-tokyo2a.svg', bbox_inches="tight")

t = (df['公表_年月日'] - df['確定_年月日']).dt.days
ax.clear()
# sns.histplot(u, discrete=True)
ax.hist(t, range(int(np.nanmin(t)), int(np.nanmax(t)) + 2),
         color="lightgray", edgecolor="black")
ax.set_xlim(0, 20)
ax.set_xticks(range(0, 25, 5))
ax.legend(['公表日-確定日 median=' + str(np.nanmedian(t))])
fig.savefig('../img/COVID-tokyo2b.svg', bbox_inches="tight")

t = (df['確定_年月日'] - df['発症_年月日']).dt.days
ax.clear()
ax.hist(t, range(int(np.nanmin(t)), int(np.nanmax(t)) + 2),
         color="lightgray", edgecolor="black")
ax.set_xlim(0, 20)
ax.set_xticks(range(0, 25, 5))
ax.legend(['確定日-発症日 median=' + str(np.nanmedian(t))])
fig.savefig('../img/COVID-tokyo2c.svg', bbox_inches="tight")

df1 = df[df['公表_年月日'] >= np.datetime64('2021-01-01')]
t = (df1['確定_年月日'] - df1['発症_年月日']).dt.days
ax.clear()
ax.hist(t, range(int(np.nanmin(t)), int(np.nanmax(t)) + 2),
         color="lightgray", edgecolor="black")
ax.set_xlim(0, 20)
ax.set_xticks(range(0, 25, 5))
ax.legend(['2021年公表 確定日-発症日 median=' + str(np.nanmedian(t))])
fig.savefig('../img/COVID-tokyo2d.svg', bbox_inches="tight")

t = (df1['公表_年月日'] - df1['確定_年月日']).dt.days
ax.clear()
ax.hist(t, range(int(np.nanmin(t)), int(np.nanmax(t)) + 2),
         color="lightgray", edgecolor="black")
ax.set_xlim(0, 20)
ax.set_xticks(range(0, 25, 5))
ax.legend(['2021年公表 公表日-確定日 median=' + str(np.nanmedian(t))])
fig.savefig('../img/COVID-tokyo2e.svg', bbox_inches="tight")

print("COVID-tokyo2.py: succeeded.")

exit()
#---

h = [np.nanmedian(t[df['確定_年月日'] == i]) for i in b]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.plot(df['確定_年月日'], t, 'ko', markersize=5, alpha=0.1, zorder=-10)
ax.plot(b, h, color='C1')
ax.set_rasterization_zorder(0) # zorder < 0 だけラスタライズする
ax.set_xlabel('確定日')
ax.set_ylabel('確定日-発症日')

fig.savefig('../img/COVID-tokyo2d.svg', bbox_inches="tight")
