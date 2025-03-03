#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy as np
import pdftotext
import requests
import urllib
import time

now = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

url = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/'
r = requests.get(url)
a = re.findall(' href="/docs/default-source/coronaviruse/situation-reports/(.*?\.pdf)', r.text)
url = 'https://www.who.int/docs/default-source/coronaviruse/situation-reports/' + a[0]

dic = {
    'United Republic of Tanzania': 'Tanzania',
    'United States of America': 'US',
    'Dominican Republic': 'Dominica',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'of)': 'Venezuela',
    'Iran (Islamic Republic of)': 'Iran',
    'United Arab Emirates': 'Arab',
    'occupied Palestinian territory': 'Palestine',
    'The United Kingdom': 'UK',
    'Russian Federation': 'Russia',
    'Republic of Moldova': 'Moldova',
    'Bosnia and Herzegovina': 'Bosnia',
    'Republic of Korea': 'Korea',
    '(Commonwealth of the)': 'Northern Mariana Islands'
}

countries = []
confirmed = []
death = []

# with open('/usr/local/junk/2020/2020-05-06/20200505covid-19-sitrep-106.pdf', 'rb') as f:
with urllib.request.urlopen(url) as f:
    for line in "".join(pdftotext.PDF(f)).split("\n"):
        line = line.strip()
        m = re.search(r'^([^\d\[]+)(\[\d\])?  +([\d]+( \d\d\d)?( \d\d\d)?)  +(-?[\d]+( \d\d\d)?( \d\d\d)?)  +([\d]+( \d\d\d)?( \d\d\d)?)  +(-?[\d]+( \d\d\d)?( \d\d\d)?) +([A-Za-z ]+)([\d]+)$', line)
        if m and m[1].strip() != 'Grand total':
            country = m[1].strip()
            if country in dic:
                country = dic[country]
            countries.append(country)
            confirmed.append(int(m[3].replace(' ', '')))
            death.append(int(m[9].replace(' ', '')))
            print(country, int(m[3].replace(' ', '')), int(m[9].replace(' ', '')))

countries = np.array(countries)
confirmed = np.array(confirmed)
death = np.array(death)

plt.figure(figsize=[6.4, 6.4])

bottom = 500

plt.clf()
plt.plot(confirmed[death >= bottom], death[death >= bottom], 'o')
plt.xscale('log')
plt.yscale('log')
plt.axis('equal')

for x in zip(confirmed[death >= bottom], death[death >= bottom], countries[death >= bottom]):
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
plt.figtext(0.9, 0.89, 'generated: ' + now, horizontalalignment='right')

plt.savefig('../img/COVID-world.svg', bbox_inches="tight")
