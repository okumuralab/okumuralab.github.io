#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/COVID-DP-hist.csv")

cmap = plt.get_cmap("tab20")
fig, ax = plt.subplots()

s = df['Symptomatic confirmed cases'].values
a = df['Asymptomatic confirmed cases'].values
t = df['Persons aboard on 5 February'].values
c = t.cumsum()

ax.bar(c, 1, width=-t, align='edge', color=cmap(15), edgecolor="white")
ax.bar(c, (s + a) / t, width=-t, align='edge', color=cmap(3), edgecolor="white")
ax.bar(c, s / t, width=-t, align='edge', color=cmap(2), edgecolor="white")
ax.set_ylim(0, 1)
ax.set_xlim(0, c[-1])
ax.set_xticks(c[1:], [20,30,40,50,60,70,80,90])

ax.legend(['Negative', 'Asymptomatic confirmed', 'Symptomatic confirmed'])

fig.savefig('../img/COVID-DP-hist.svg', bbox_inches="tight")
