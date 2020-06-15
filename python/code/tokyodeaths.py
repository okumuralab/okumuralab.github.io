#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('../data/tokyodeaths.csv')

def days(year, month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1] + ((month == 2) and
                           ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)))

perday = np.array([r[2] / days(r[0], r[1]) for i, r in df.iterrows()])

for y in range(2010, 2020):
    plt.plot(df[df['year'] == y]['month'], perday[df['year'] == y], 'o-k', alpha=0.2)
plt.plot(df[df['year'] == 2011]['month'], perday[df['year'] == 2011], 'o-', label='2011')
plt.plot(df[df['year'] == 2020]['month'], perday[df['year'] == 2020], 'o-', label='2020')
plt.legend()
plt.savefig('../img/tokyodeaths1.svg', bbox_inches="tight")

plt.clf()
plt.plot(df[df['month'] == 1]['year'], perday[df['month'] == 1], 'o-', label='Jan')
plt.plot(df[df['month'] == 2]['year'], perday[df['month'] == 2], 'o-', label='Feb')
plt.plot(df[df['month'] == 3]['year'], perday[df['month'] == 3], 'o-', label='Mar')
plt.plot(df[df['month'] == 4]['year'], perday[df['month'] == 4], 'o-', label='Apr')
plt.legend()
plt.savefig('../img/tokyodeaths2.svg', bbox_inches="tight")

