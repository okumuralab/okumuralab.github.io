#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/COVID-DP-hist.csv")

cmap = plt.get_cmap("tab20")

plt.clf()
plt.bar(df['Persons aboard on 5 February'].cumsum(),
        1,
        width=-df['Persons aboard on 5 February'].values,
        align='edge', color=cmap(15), edgecolor="white")
plt.bar(df['Persons aboard on 5 February'].cumsum(),
        (df['Symptomatic confirmed cases'] + df['Asymptomatic confirmed cases'])
        / df['Persons aboard on 5 February'],
        width=-df['Persons aboard on 5 February'].values,
        align='edge', color=cmap(3), edgecolor="white")
plt.bar(df['Persons aboard on 5 February'].cumsum(),
        df['Symptomatic confirmed cases'] / df['Persons aboard on 5 February'],
        width=-df['Persons aboard on 5 February'].values,
        align='edge', color=cmap(2), edgecolor="white")
plt.ylim(0, 1)
plt.xlim(0, df['Persons aboard on 5 February'].cumsum().values[-1])
plt.xticks(df['Persons aboard on 5 February'].cumsum()[1:],
           [20,30,40,50,60,70,80,90])

plt.savefig('../img/COVID-DP-hist.svg', bbox_inches="tight")
