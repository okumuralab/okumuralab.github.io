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

# 再陽性を削除
pp = ['再陽性' not in x for x in df['備考'].astype(str)]
df = df[pp].copy()

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

ax.plot(df['確定日'], dt, 'ko', markersize=5, alpha=0.1, zorder=-10)
ax.plot(b, h, color='C1')
ax.set_rasterization_zorder(0) # zorder < 0 だけラスタライズする
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
# 平均年代の推移

# df1 = df[(df['受診都道府県'] == '東京都') & (df['年代'] != '不明')]
df1 = df[(df['年代'].astype(str) != '不明') & (df['年代'].astype(str) != 'nan')].copy()
# df1['年代'].value_counts(sort=False)
df1.loc[df1['年代'] == '0-10', '年代'] = 0
df1['年代'] = df1['年代'].astype(int)

b = np.arange(datetime.datetime(2020,3,1),
              max(df1['確定日']) + datetime.timedelta(days=1),
              datetime.timedelta(days=1))

a = []
for i in b:
    df2 = df1[df1['確定日'] == i]
    y = df2['年代'].values
    if len(y) >= 10:
        a.append(np.mean(y) + 5)
    else:
        a.append(np.nan)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.plot(b, a, 'o-')
ax.set_ylabel('平均年代')
# ax.legend(['東京'])
ax.legend(['全国'])

fig.savefig('../img/200312j.svg', bbox_inches="tight")

#-----

exit()

#-----

df1 = df[df['受診都道府県'] == '大阪府']

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.hist(df1['発症日'], bins=b, edgecolor="black", alpha=0.5)
ax.hist(df1['確定日'], bins=b, edgecolor="black", alpha=0.5)
ax.set_xlim(datetime.datetime(2020,3,20), datetime.datetime(2020,5,1))
ax.legend(['発症日 (onset)', '確定日 (confirmed)'])

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
# 年代分布

df1 = df[(df['受診都道府県'] == '東京都') & (df['年代'] != '不明')]
# df1['年代'].value_counts(sort=False)
df1['年代'][df1['年代'] == '0-10'] = 0
df1['年代'] = df1['年代'].astype(int)

ax.clear()
# ax.hist(df1['年代'], bins=range(0,110,10), edgecolor="black")
ax.hist(df1['年代'][(df1['確定日'] >= datetime.datetime(2020,4,1)) & (df1['確定日'] < datetime.datetime(2020,5,1))], bins=range(0,110,10), color='gray', edgecolor="black")
ax.set_xlabel('年代')
ax.set_ylabel('人数')
plt.legend(['東京 4月'])

ax.clear()
ax.hist(df1['年代'][df1['確定日'] >= datetime.datetime(2020,6,1)], bins=range(0,110,10), color='gray', edgecolor="black")
ax.set_xlabel('年代')
ax.set_ylabel('人数')
plt.legend(['東京 6月以降'])
