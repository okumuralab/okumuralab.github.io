#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv("../data/japandeaths.csv")
t = [datetime.datetime(int(x["年"]), int(x["月"]), 1) for i, x in df.iterrows()]

def days(year, month=None):
    year = int(year)
    leap = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    if month is None:
        return 365 + leap
    else:
        month = int(month)
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return m[month - 1] + ((month == 2) and leap)

perday1 = np.array([r[2] / days(r[0], r[1]) for i, r in df.iterrows()]) # 確定数
perday2 = np.array([r[3] / days(r[0], r[1]) for i, r in df.iterrows()]) # 概数
perday3 = np.array([r[4] / days(r[0], r[1]) for i, r in df.iterrows()]) # 速報値

plt.clf()
plt.plot(t, perday1, "o-")
plt.plot(t, perday2, "s-")
plt.plot(t, perday3, "*-")
plt.ylabel("1日あたり死亡数")
plt.legend(["確定数", "概数", "速報値"])
plt.show()
plt.savefig("../img/japandeaths1.svg", bbox_inches="tight")

df["死亡数"] = [n3 if np.isnan(n1) and np.isnan(n2) else n2 if np.isnan(n1) else n1
                for n1, n2, n3 in zip(df["確定数"], df["概数"], df["速報値"])]
df["日数"] = [days(year, month) for year, month in zip(df["年"], df["月"])]

plt.clf()
for y in sorted(set(df["年"])):
    df1 = df[df["年"] == y]
    plt.plot(df1["月"], df1["死亡数"] / df1["日数"],
             alpha=0.5, marker=f"${y % 10}$", label=y)
plt.xlabel("月")
plt.ylabel("1日あたり死亡数")
plt.legend(loc=(0.38, 0.60), labelspacing=0.1)
plt.show()
plt.savefig("../img/japandeaths2.svg", bbox_inches="tight")

plt.clf()
for m in range(1, 13):
    df1 = df[df["月"] == m]
    plt.plot(df1["年"], df1["死亡数"] / df1["日数"], marker=f"${m}$")
plt.ylabel("1日あたり死亡数")
plt.xticks(sorted(set(df["年"] // 2 * 2).intersection(set(df["年"]))))
plt.show()
plt.savefig("../img/japandeaths3.svg", bbox_inches="tight")

df1 = df.groupby("年")[["死亡数", "日数"]].sum()
df2 = df1[df1.index < 2022]
y = df2.index
x = df2["死亡数"] / df2["日数"]

plt.clf()
plt.plot(y, x, "o-")
plt.xlabel("年")
plt.ylabel("1日あたり死亡数")
plt.show()
plt.savefig("../img/japandeaths4.svg", bbox_inches="tight")

u = (2012 <= y) & (y <= 2019)
slope, intercept = np.polyfit(y[u], x[u], 1)
plt.clf()
plt.plot(y, x - (slope * y + intercept), "o-")
plt.axhline(linewidth=0.5, color="black")
plt.xlabel("年")
plt.ylabel("1日あたり超過死亡数")
plt.plot([2020, 2021], [3459 / 366, (18385 - 3459) / 365], "o-")
plt.show()
plt.savefig("../img/japandeaths5.svg", bbox_inches="tight")

df3 = df.query("月 <= 4").groupby("年")[["死亡数", "日数"]].sum()
y = df3.index
x = df3["死亡数"] / df3["日数"]

plt.clf()
plt.plot(y, x, "o-")
plt.xlabel("年")
plt.ylabel("1〜4月の1日あたり死亡数")
plt.xticks(sorted(set(y // 2 * 2).intersection(set(y))))  # 2年ごと
plt.show()
plt.savefig("../img/japandeaths6.svg", bbox_inches="tight")

exit()

#------

df = pd.read_csv("deaths_cumulative_daily.csv", parse_dates=['Date'])
a = np.arange(np.datetime64("2020-06"), np.datetime64("2022-10"))
da = pd.to_datetime(a)
da1 = da - np.timedelta64(1,"D")
da1s = pd.Series(da1, name='Date')
df2 = pd.merge(da1s, df).diff()
x = df2.ALL / (df2.Date / np.timedelta64(1,"D"))
for i in range(1, len(x)):
    print(f"{a[i-1]},{x[i]:3.1f}")
