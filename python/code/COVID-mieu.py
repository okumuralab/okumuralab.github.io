#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv("../data/COVID-mieu.csv", parse_dates=['date'])

# df['students'].sum() # 65
# df['others'].sum()   #  4

fig, ax = plt.subplots(figsize=(10, 3))
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)

ax.clear()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
bottom = 0
for x in ['others', 'students']:
    ax.bar(df['date'], df[x], width=1, bottom=bottom,
           align='edge', edgecolor="black", linewidth=0.5,
           label=x + ' (' + str(df[x].sum()) + ')')
    bottom += df[x]
ax.legend()
plt.savefig('../img/COVID-mieu.svg', bbox_inches="tight")
