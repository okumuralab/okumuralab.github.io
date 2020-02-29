#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-DP.csv", index_col='Date', parse_dates=['Date'])

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df.index, df['Examined'])
ax.bar(df.index, df['Positive'])
plt.legend(['Negative', 'Positive'])
plt.savefig('../img/COVID-DP.svg', bbox_inches="tight")

#-----

import numpy as np
from statsmodels.stats.proportion import proportion_confint

plt.clf()

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

p = [x['Positive'] / x['Examined'] for i, x in df.iterrows()]
ci0, ci1 = np.array([proportion_confint(x['Positive'], x['Examined'], method='beta')
                     for i, x in df.iterrows()]).T
ax.errorbar(df.index, p, [p - ci0, ci1 - p], fmt="o", capsize=5, color="C1")
ax.grid(axis='y')

plt.savefig('../img/COVID-DP-rate.svg', bbox_inches="tight")
