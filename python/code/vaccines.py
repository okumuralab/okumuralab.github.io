#! /usr/local/bin/python3

import os
import re
import time
import subprocess
import matplotlib.pyplot as plt
import pandas as pd

# URL2 = "https://www.kantei.go.jp/jp/content/IRYO-vaccination_data3.xlsx"
# URL3 = "https://www.kantei.go.jp/jp/content/KOREI-vaccination_data3.xlsx"
URL = "https://www.kantei.go.jp/jp/content/vaccination_data5.xlsx"

def filename(url):
    return re.sub("^.*/", "", url)

def wget(url):
    try:
        t = os.stat(filename(url)).st_mtime
    except:
        t = 0
    if time.time() - t < 3600 * 10:  # 10時間より新しければ再取得しない
        return False
    r = subprocess.run(["wget", "-N", url],
                       capture_output=True, text=True,
                       env={"PATH": "/usr/local/bin:/usr/bin", "LANG": "en"})
    return " saved " in r.stderr

t = wget(URL)

if not t:
    exit()

df1 = pd.read_csv("../data/vaccines.csv", parse_dates=['日付'])
df2 = pd.read_excel(filename(URL), sheet_name="医療従事者等",
                   header=None, skiprows=5,
                   usecols="A,D,E,F,G").dropna(thresh=3).fillna(0)
df3 = pd.read_excel(filename(URL), sheet_name="一般接種",
                   header=None, skiprows=6,
                   usecols="A,D,E,F,G,H,I").dropna(thresh=3).fillna(0)

skip = 5
while skip < 100:
    df5 = pd.read_excel(filename(URL), sheet_name="総接種回数",
                        header=None, skiprows=skip,
                        usecols="A,I").dropna().fillna(0)
    if df5.index[0] == 0 and type(df5[0][0]) == pd.Timestamp:
        break
    skip += 1

if skip == 100:
    print("Something is wrong.")
    exit(1)

df5[8] = df5[8].diff(-1).fillna(df5[8].values[-1])
df2.iloc[:, 1] += df2.iloc[:, 2]
df2.iloc[:, 3] += df2.iloc[:, 4]
df3.iloc[:, 1] += df3.iloc[:, 2]
df3.iloc[:, 1] += df3.iloc[:, 3]
df3.iloc[:, 4] += df3.iloc[:, 5]
df3.iloc[:, 4] += df3.iloc[:, 6]
df4 = pd.merge(df2, df3, how="outer", on=0).fillna(0)
df4 = pd.merge(df4, df5, how="outer", on=0).fillna(0)
df4.columns = ['日付', '医療従事者1回目', 'A', '医療従事者2回目', 'B',
               'その他1回目', 'C', 'D', 'その他2回目', 'E', 'F', '3回目']
df = pd.merge(df1, df4, how="outer").fillna(0)
# df.columns = ['日付', '医療従事者等1回目', '医療従事者等2回目', '一般接種1回目', '一般接種2回目', 'A', 'B', 'C', 'D', 'E', 'F']

bottom = 0
for c in df.columns[[11, 4, 3, 2, 1]]:
    plt.bar(df['日付'], df[c], bottom=bottom, label=c) # edgecolor="white", linewidth=0.1
    bottom += df[c]
plt.legend()
plt.xticks(rotation=20)

plt.savefig('../img/mhlw-vaccine.svg', bbox_inches="tight")

print("mhlw-vaccine.svg generated.")
