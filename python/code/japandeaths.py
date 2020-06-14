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

perday1 = np.array([r[2] / days(r[0], r[1]) for i, r in df.iterrows()])
perday2 = np.array([r[3] / days(r[0], r[1]) for i, r in df.iterrows()])

plt.plot(t, perday1, 'o-')
plt.plot(t, perday2, 'o-')
plt.ylabel('1日あたり死亡数')
plt.legend(['確定値', '速報値'])

plt.savefig('../img/japandeaths1.svg', bbox_inches="tight")

plt.clf()
for y in range(2014, 2020):
    plt.plot(df[df['年'] == y]['月'], perday1[df['年'] == y],
             'o-', alpha=0.5, marker=f'${y % 10}$', label=y)

plt.plot(df[df['年'] == 2019]['月'], perday2[df['年'] == 2019],
         'o-', marker='$9$', label='2019速報値')
plt.plot(df[df['年'] == 2020]['月'], perday2[df['年'] == 2020],
         'o-k', label='2020速報値')
plt.xlabel('月')
plt.ylabel('1日あたり死亡数')
plt.legend()
plt.savefig('../img/japandeaths2.svg', bbox_inches="tight")

plt.clf()
plt.plot(df[df['月'] == 1]['年'], perday1[df['月'] == 1], 'o-', label='Jan')
plt.plot(df[df['月'] == 2]['年'], perday1[df['月'] == 2], 'o-', label='Feb')
plt.plot(df[df['月'] == 3]['年'], perday1[df['月'] == 3], 'o-', label='Mar')
plt.plot(df[df['月'] == 1]['年'], perday2[df['月'] == 1], 'o-', color='C0')
plt.plot(df[df['月'] == 2]['年'], perday2[df['月'] == 2], 'o-', color='C1')
plt.plot(df[df['月'] == 3]['年'], perday2[df['月'] == 3], 'o-', color='C2')
plt.ylabel('1日あたり死亡数')
plt.legend()
plt.savefig('../img/japandeaths3.svg', bbox_inches="tight")