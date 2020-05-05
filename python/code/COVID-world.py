#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy as np
import pdftotext
import requests
import urllib

url = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/'
r = requests.get(url)
a = re.findall(' href="(.*?\.pdf)', r.text)
if a[0][0] == '/':
    url = 'https://www.who.int' + a[0]
elif a[0][0:8] == 'https://':
    url = a[0]
else:
    url = url + a[0]

dic = {
    'Republic of)': 'Iran',
    'of)': 'Iran',
    'Iran (Islamic': 'Iran',
    'Iran (Islamic Republic of)': 'Iran',
    'Iran (Islamic Republic': 'Iran',
    'Emirates': 'Arab',
    'United Arab': 'Arab',
    'United Arab Emirates': 'Arab',
    'Occupied': 'Palestine',
    'Palestinian Territory': 'Palestine',
    'occupied Palestinian': 'Palestine',
    'territory': 'Palestine',
    'United States of': 'US',
    'the United States': 'US',
    'United States of America': 'US',
    'America': 'US',
    'Republic of Korea': 'Korea',
    'the United': 'UK',
    'the United Kingdom': 'UK',
    'The United Kingdom': 'UK',
    'of the Congo': 'Congo',
    'State of)': 'Bolivia',
    'Herzegovina': 'Bosnia',
    'Bosnia and': 'Bosnia',
    'International': '(Diamond Princess)',
    'conveyance': '(Diamond Princess)',
    'International conveyance': '(Diamond Princess)',
    'Saint Barthélemy': 'Saint Barthelemy',
}

countries = []
confirmed = []
death = []

prev = ''
with urllib.request.urlopen(url) as f:
    for line in "".join(pdftotext.PDF(f)).split("\n"):
        line = line.strip()
        # m = re.search(r'^Total +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+)$', line)
        # if m:
        #     countries.append('China')
        #     confirmed.append(int(m[5]))
        #     death.append(int(m[6]))
        m = re.search(r'^([^\d]+)?(\d+) +(-?\d+) +(\d+) +(-?\d+) +([A-Za-z ]+)(\d+)$', line)
        if m and m[1] and m[1].strip() != 'Grand total':
            print(line)
            country = m[1].strip()
            if country in dic:
                country = dic[country]
            countries.append(country)
            confirmed.append(int(m[2]))
            death.append(int(m[4]))
        prev = line

countries = np.array(countries)
confirmed = np.array(confirmed)
death = np.array(death)

plt.figure(figsize=[6.4, 6.4])

bottom = 100

# plt.clf()
plt.plot(confirmed[death >= bottom], death[death >= bottom], 'o')
plt.xscale('log')
plt.yscale('log')
plt.axis('equal')

for x in zip(confirmed[death >= bottom], death[death >= bottom], countries[death >= bottom]):
    if len(x[2]) == 2 or len(x[2]) == 5:
        plt.text(x[0], x[1], x[2], horizontalalignment='right', verticalalignment='top')
    else:
        plt.text(x[0], x[1], x[2], horizontalalignment='left', verticalalignment='bottom')

plt.xlabel('Confirmed')
plt.ylabel('Deaths')

plt.autoscale(False)

df1 = pd.read_csv("../data/COVID-19.csv",
                  index_col='Date', parse_dates=['Date'])
plt.plot(df1['China Confirmed'], df1['China Deaths'], 'x-')

df2 = pd.read_csv("../data/COVID-jp.csv",
                  index_col='Date', parse_dates=['Date'])
plt.plot(df2['Confirmed'], df2['Deaths'], 'x-')

x = np.array([min(confirmed[death >= bottom]), max(confirmed[death >= bottom])])
y = x * df1['China Deaths'][-1] / df1['China Confirmed'][-1]
plt.plot(x, y, color='lightgray', label=f"Deaths / Confirmed = {df1['China Deaths'][-1] / df1['China Confirmed'][-1]:.4f}")

plt.legend(loc='upper left')

plt.savefig('../img/COVID-world.svg', bbox_inches="tight")
