#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportion_confint

df = pd.read_csv("../data/COVID-mhlw.csv", index_col='Date', parse_dates=['Date'])

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.bar(df.index, df['Examined'])
ax.bar(df.index, df['Confirmed'])
plt.legend(['Negative', 'Positive'])

plt.savefig('../img/COVID-mhlw2.svg', bbox_inches="tight")

plt.clf()
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax = plt.gca()  # または ax = plt.subplot(1,1,1)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

p = [x['Confirmed'] / x['Examined'] for i, x in df.iterrows()]
ci0, ci1 = np.array([proportion_confint(x['Confirmed'], x['Examined'], method='beta')
                     for i, x in df.iterrows()]).T
ax.errorbar(df.index, p, [p - ci0, ci1 - p], fmt="o", capsize=5)
ax.grid(axis='y')

plt.savefig('../img/COVID-mhlw.svg', bbox_inches="tight")
