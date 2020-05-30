#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import datetime
import time

df = pd.read_csv("https://dl.dropboxusercontent.com/s/6mztoeb6xf78g5w/COVID-19.csv",
                 parse_dates=['確定日', '発症日'], low_memory=False)
now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

b = np.arange(min(min(df['確定日']), min(df['発症日'])),
              max(max(df['確定日']), max(df['発症日'])) + datetime.timedelta(days=2),
              datetime.timedelta(days=1))

fig, ax = plt.subplots()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

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

#-----

df1 = df[df['受診都道府県'] == '東京都']

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.hist(df1['発症日'], bins=b, edgecolor="black", alpha=0.5)
ax.hist(df1['確定日'], bins=b, edgecolor="black", alpha=0.5)
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312g.svg', bbox_inches="tight")

#-----

df1 = df[df['受診都道府県'] != '東京都']

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.hist(df1['発症日'], bins=b, edgecolor="black", alpha=0.5)
ax.hist(df1['確定日'], bins=b, edgecolor="black", alpha=0.5)
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312h.svg', bbox_inches="tight")

exit()

#-----

df1 = df[df['受診都道府県'] != '東京都']
# df1 = df[(df['受診都道府県'] != '東京都') & (df['発症日'] == datetime.datetime(2020,4,1))]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.hist(df1['発症日'], bins=b, edgecolor="black", alpha=0.5)
ax.hist(df1['確定日'], bins=b, edgecolor="black", alpha=0.5)
ax.set_xlim(datetime.datetime(2020,3,20), datetime.datetime(2020,5,1))
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

fig.savefig('../img/200312i.svg', bbox_inches="tight")

#-----

ken = ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]

for k in ken:
    ax.clear()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    df1 = df[df['受診都道府県'] == k]
    ax.hist(df1['発症日'], bins=b, edgecolor="black", alpha=0.5)
    ax.hist(df1['確定日'], bins=b, edgecolor="black", alpha=0.5)
    ax.legend(['発症日 (onset)', '確定日 (confirmed)'])
    fig.savefig(k + '.svg', bbox_inches="tight")

#-----
