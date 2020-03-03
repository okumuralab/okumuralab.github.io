#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/COVID-DP-hist.csv")

cmap = plt.get_cmap("tab20")

s = df['Symptomatic confirmed cases'].values
a = df['Asymptomatic confirmed cases'].values
t = df['Persons aboard on 5 February'].values
c = t.cumsum()

plt.clf()
plt.bar(c, 1, width=-t, align='edge', color=cmap(15), edgecolor="white")
plt.bar(c, (s + a) / t, width=-t, align='edge', color=cmap(3), edgecolor="white")
plt.bar(c, s / t, width=-t, align='edge', color=cmap(2), edgecolor="white")
plt.ylim(0, 1)
plt.xlim(0, c[-1])
plt.xticks(c[1:], [20,30,40,50,60,70,80,90])

plt.legend(['Negative', 'Asymptomatic confirmed', 'Symptomatic confirmed'])

plt.savefig('../img/COVID-DP-hist.svg', bbox_inches="tight")
