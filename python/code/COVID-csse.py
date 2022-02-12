#! /usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import time

URLC = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
URLD = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

df = pd.read_csv(URLC)

df = df.groupby('Country/Region').sum().iloc[:, 2:]
t = pd.to_datetime(df.columns)

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

fig, ax = plt.subplots(figsize=[7, 7])
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

for country in df.index:
    if df.loc[country][-1] > 1000:
        ax.plot(t, df.loc[country])
        ax.text(t[-1], df.loc[country][-1], country)
ax.plot(t, df.loc['Japan'], 'o-k', label='Japan')

ax.set_yscale('log')
ax.set_ylim(1000)

ax.set_ylabel('Confirmed')
ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

dfa = df.diff(axis=1).rolling(7, axis=1).mean()

o = np.argsort(-dfa.iloc[:, -1])

for country in np.append(df.index[o][:7], 'Japan'):
    ax.plot(t, dfa.loc[country], 'o-', label=country)
    ax.text(t[-1], dfa.loc[country][-1], country)
ax.set_ylabel('Confirmed')
ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse1.svg', bbox_inches="tight")

#-----

df = pd.read_csv(URLD)

df = df.groupby('Country/Region').sum().iloc[:, 2:]
t = pd.to_datetime(df.columns)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

for country in df.index:
    if df.loc[country][-1] > 10:
        ax.plot(t, df.loc[country])
        ax.text(t[-1], df.loc[country][-1], country)
ax.plot(t, df.loc['Japan'], 'o-k', label='Japan')

ax.set_yscale('log')
ax.set_ylim(10)

ax.set_ylabel('Deaths')
ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse2.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

dfa = df.diff(axis=1).rolling(7, axis=1).mean()

o = np.argsort(-dfa.iloc[:, -1])

for country in np.append(df.index[o][:7], 'Japan'):
    ax.plot(t, dfa.loc[country], 'o-', label=country)
    ax.text(t[-1], dfa.loc[country][-1], country)

ax.set_ylabel('Deaths')
ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse3.svg', bbox_inches="tight")
