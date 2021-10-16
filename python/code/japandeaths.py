#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('../data/japandeaths.csv')
t = [datetime.datetime(int(x['年']), int(x['月']), 1) for i, x in df.iterrows()]

def days(year, month):
    year = int(year)
    month = int(month)
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1] + ((month == 2) and
                           ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)))

perday1 = np.array([r[2] / days(r[0], r[1]) for i, r in df.iterrows()]) # 確定数
perday2 = np.array([r[3] / days(r[0], r[1]) for i, r in df.iterrows()]) # 概数
perday3 = np.array([r[4] / days(r[0], r[1]) for i, r in df.iterrows()]) # 速報値

plt.clf()
plt.plot(t, perday1, 'o-')
plt.plot(t, perday2, 's-')
plt.plot(t, perday3, '*-')
plt.ylabel('1日あたり死亡数')
plt.legend(['確定数', '概数', '速報値'])

plt.savefig('../img/japandeaths1.svg', bbox_inches="tight")

plt.clf()
for y in range(2014, 2021):
    plt.plot(df[df['年'] == y]['月'], perday1[df['年'] == y],
             alpha=0.5, marker=f'${y % 10}$', label=y)
plt.plot(df[df['年'] == 2021]['月'], perday2[df['年'] == 2021],
         'k', marker='$1$', alpha=0.5, label='2021概数')
plt.plot(df[df['年'] == 2021]['月'], perday3[df['年'] == 2021],
         'o-k', label='2021速報値')
plt.xlabel('月')
plt.ylabel('1日あたり死亡数')
plt.legend(loc=(0.45,0.48))
plt.savefig('../img/japandeaths2.svg', bbox_inches="tight")

perday = np.array([p3 if np.isnan(p1) and np.isnan(p2) else p2 if np.isnan(p1) else p1 for p1, p2, p3 in zip(perday1, perday2, perday3)])
plt.clf()
for m in range(1, 13):
    plt.plot(df[df['月'] == m]['年'], perday[df['月'] == m], marker=f'${m}$')
plt.ylabel('1日あたり死亡数')
plt.savefig('../img/japandeaths3.svg', bbox_inches="tight")
