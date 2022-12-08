#! /usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import time
import json
import twitter
import os

def readcsv(url):
    try:
        df = pd.read_csv(url, parse_dates=[0], thousands=",")
        print('utf-8:', url)
    except UnicodeDecodeError:
        df = pd.read_csv(url, parse_dates=[0], thousands=",", encoding='cp932')
        print('cp932:', url)
    return df

now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())
nowdate = time.strftime('%Y-%m-%d', time.localtime())

# 新規陽性者数の推移（日別）
for i in range(60):
    df2 = readcsv("https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv")
    if pd.Timestamp(df2['Date'].values[-1]).strftime("%Y-%m-%d") >= nowdate:
        break
    time.sleep(60)  # wait 1 minute

if pd.Timestamp(df2['Date'].values[-1]).strftime("%Y-%m-%d") < nowdate:
    print("Timed out")
    exit()

confirmed = df2['Tokyo'].values[-1]
MYURL = "https://okumuralab.org/~okumura/python/COVID-19.html"
status = f"今日の東京は{confirmed}人 {MYURL}"
print(status)
FILE = "/home/okumura/public_html/python/data/COVID-tokyo.csv"
with open(FILE, "a") as f:
    f.write(f"{nowdate},{confirmed}\n")
os.system("cd /home/okumura/public_html/python/code && ./COVID-tokyo.py")
with open("/home/okumura/.twitter.json") as f:
    token = json.load(f)
api = twitter.Api(consumer_key=token["consumer_key"],
                  consumer_secret=token["consumer_secret"],
                  access_token_key=token["access_token"],
                  access_token_secret=token["access_token_secret"],
                  tweet_mode='extended',
                  sleep_on_rate_limit=True)
# ツイート
r = api.PostUpdate(
    status, # ツイート本文
    media=[
        "/home/okumura/public_html/python/img/COVID-tokyo-a.png",
        "/home/okumura/public_html/python/img/COVID-tokyo-rt.png"
    ],
    latitude=34.7468, longitude=136.5248, # 位置情報
    display_coordinates=True # 正確な位置情報にする
)
print(f"https://twitter.com/h_okumura/status/{r.id}")
os.system("rsync -e 'ssh -p 59224' -auvz /home/okumura/public_html/python/data/COVID-tokyo.csv oku.edu.mie-u.ac.jp:public_html/python/data/")


# PCR検査実施人数
df1 = readcsv("https://www.mhlw.go.jp/content/pcr_tested_daily.csv")

# 死亡者数（累積）
df3 = readcsv("https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv")

fig, ax = plt.subplots()
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df1.iloc[:,0], df1.iloc[:,1], width=1)
ax.bar(df2['Date'], df2['ALL'], width=1)
ax.legend(['Negative', 'Positive'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen1.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df2['Date'], df2['ALL'], width=1, color='C1')
ax.bar(df3['Date'], df3['ALL'].diff(), width=1, color='C3')
ax.legend(['Positive', 'Deaths'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen2.svg', bbox_inches="tight")

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df3['Date'], df3['ALL'].diff(), width=1, color='C3')
ax.legend(['Deaths'], loc='upper left')
fig.savefig('../img/COVID-mhlwopen3.svg', bbox_inches="tight")
