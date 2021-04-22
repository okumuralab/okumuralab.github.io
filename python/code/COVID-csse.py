#! /usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from dateutil.parser import parse
import time

URLC = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
URLD = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

df = pd.read_csv(URLC)
now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

t = [parse(i) for i in df.columns[4:]]
x = [df.groupby('Country/Region')[i].sum() for i in df.columns[4:]]

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

fig, ax = plt.subplots(figsize=[7, 7])
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')
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
ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

dx = np.diff(x, axis=0)
o = np.argsort(-np.mean(dx[-8:-1], axis=0))

for i in np.append(o[:7], list(x[0].index).index('Japan')):
    ax.plot(t[1:], dx[:,i], 'o-', label=x[0].index[i])
    ax.text(t[-1], dx[-1,i], x[0].index[i])
ax.set_ylabel('Confirmed')
ax.legend(loc='upper left')
ax.set_ylim(0, 310000)

# dx = np.diff(np.array(x, dtype=np.float), axis=0)
# dx[21][x[-1].index == 'China'] = np.nan
# ax.plot(t[1:], dx, 'o-', zorder=-10)
# ax.set_yscale('log')

# j = 0
# for i in x[-1].index:
#     # if dx[-1][j] > 500:
#     ax.text(t[-1], dx[-1][j], i, zorder=-10)
#     j += 1
    
# # ax.legend(x[-1].index)

# japan = [x[i]['Japan'] for i in range(len(x))]
# ax.plot(t[1:], np.diff(japan), 'o-k', label='Japan', zorder=-10)
# ax.set_rasterization_zorder(0) # zorder < 0 だけラスタライズする
# ax.set_ylabel('Confirmed')
# ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse1.svg', bbox_inches="tight")

#-----

df2 = pd.read_csv(URLD)

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
ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse2.svg', bbox_inches="tight")

#-----

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

dx = np.diff(x, axis=0)
o = np.argsort(-np.mean(dx[-8:-1], axis=0))

for i in np.append(o[:7], list(x[0].index).index('Japan')):
    ax.plot(t[1:], dx[:,i], 'o-', label=x[0].index[i])
    ax.text(t[-1], dx[-1,i], x[0].index[i])
ax.set_ylabel('Deaths')
ax.legend(loc='upper left')
ax.set_ylim(0)

# dx = np.diff(np.array(x, dtype=np.float), axis=0)
# ax.plot(t[1:], dx, 'o-', zorder=-10)
# # ax.set_yscale('log')

# j = 0
# for i in x[-1].index:
#     # if dx[-1][j] > 20:
#     ax.text(t[-1], dx[-1][j], i)
#     j += 1
    
# # ax.legend(x[-1].index)

# japan = [x[i]['Japan'] for i in range(len(x))]
# ax.plot(t[1:], np.diff(japan), 'o-k', label='Japan', zorder=-10)
# ax.set_rasterization_zorder(0) # zorder < 0 だけラスタライズする
# ax.set_ylabel('Deaths')
# ax.set_ylim(-100)
# ax.legend(loc='upper left')

fig.savefig('../img/COVID-csse3.svg', bbox_inches="tight")

#-----

exit()

#-----

fig, ax = plt.subplots()
fig.text(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

t1 = [parse(i) for i in df.columns[4:]]
x1 = [df.groupby('Country/Region')[i].sum() for i in df.columns[4:]]

t2 = [parse(i) for i in df2.columns[4:]]
x2 = [df2.groupby('Country/Region')[i].sum() for i in df2.columns[4:]]

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

country = 'Chile'

cnf = [x1[i][country] for i in range(len(x1))]
# ax.plot(t1[1:], np.diff(cnf), 'o-', label=country + ' confirmed')
ax.bar(t1[1:], np.diff(cnf), align='edge', color='C1',
       width=pd.Timedelta(days=1), label=country + ' confirmed')

dth = [x2[i][country] for i in range(len(x1))]
# ax.plot(t2[1:], np.diff(dth), 'o-', label=country + ' deaths')
ax.bar(t2[1:], np.diff(dth), align='edge', color='C3',
       width=pd.Timedelta(days=1), label=country + ' deaths')

ax.set_xlim(parse('2020-03-01'))
ax.legend()
