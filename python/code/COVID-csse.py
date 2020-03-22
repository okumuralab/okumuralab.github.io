#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from dateutil.parser import parse

url = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'

df = pd.read_csv(url)

t = [parse(i) for i in df.columns[4:]]
x = [df.groupby('Country/Region')[i].sum() for i in df.columns[4:]]

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

fig, ax = plt.subplots(figsize=[7, 7])

# ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.plot(t, x)
ax.set_yscale('log')

for i in x[-1].index:
    if x[-1][i] > 0:
        ax.text(t[-1], x[-1][i], i)

# ax.legend(x[-1].index)

japan = [x[i]['Japan'] for i in range(len(x))]
ax.plot(t, japan, 'o-k', label='Japan')
ax.set_ylabel('Confirmed')
ax.legend()

fig.savefig('../img/COVID-csse.svg', bbox_inches="tight")

#-----

url2 = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'

df2 = pd.read_csv(url2)

t = [parse(i) for i in df2.columns[4:]]
x = [df2.groupby('Country/Region')[i].sum() for i in df2.columns[4:]]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.plot(t, x)
ax.set_yscale('log')

for i in x[-1].index:
    if x[-1][i] > 0:
        ax.text(t[-1], x[-1][i], i)

# ax.legend(x[-1].index)

japan = [x[i]['Japan'] for i in range(len(x))]
ax.plot(t, japan, 'o-k', label='Japan')
ax.set_ylabel('Deaths')
ax.legend()

fig.savefig('../img/COVID-csse2.svg', bbox_inches="tight")

