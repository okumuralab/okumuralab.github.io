#! /usr/local/bin/python3

import os
import re
import time
import subprocess
import matplotlib.pyplot as plt
import pandas as pd

URL2 = "https://www.kantei.go.jp/jp/content/IRYO-vaccination_data.xlsx"
URL3 = "https://www.kantei.go.jp/jp/content/KOREI-vaccination_data.xlsx"

def filename(url):
    return re.sub("^.*/", "", url)

def wget(url):
    try:
        t = os.stat(filename(url)).st_mtime
    except:
        t = 0
    if time.time() - t < 3600 * 20:  # 20時間より新しければ再取得しない
        return False
    r = subprocess.run(["wget", "-N", url],
                       capture_output=True, text=True,
                       env={"PATH": "/usr/local/bin:/usr/bin", "LANG": "en"})
    return " saved " in r.stderr

t2 = wget(URL2)
t3 = wget(URL3)
if not (t2 or t3):
    exit()

df1 = pd.read_csv("../data/vaccines.csv", parse_dates=['日付'])
df2 = pd.read_excel("IRYO-vaccination_data.xlsx",
                   header=None, skiprows=4,
                   usecols="A,D,E").dropna()
df3 = pd.read_excel("KOREI-vaccination_data.xlsx",
                   header=None, skiprows=4,
                   usecols="A,D,E").dropna()
df4 = pd.merge(df2, df3, how="outer", on=0).fillna(0)
df4.columns = ['日付', '医療従事者1回目', '医療従事者2回目',
               'その他1回目', 'その他2回目']
df = pd.merge(df1, df4, how="outer").fillna(0)

bottom = 0
for c in df.columns[1:]:
    plt.bar(df['日付'], df[c], bottom=bottom, label=c)
    bottom += df[c]
plt.legend()
plt.xticks(rotation=20)

plt.savefig('../img/mhlw-vaccine.svg', bbox_inches="tight")

print("mhlw-vaccine.svg generated.")
