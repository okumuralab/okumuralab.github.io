#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/vaccines.csv", parse_dates=['日付'])

bottom = 0
for c in df.columns[1:]:
    plt.bar(df['日付'], df[c], bottom=bottom, label=c)
    bottom += df[c]
plt.legend()
plt.xticks(rotation=20)

plt.savefig('../img/mhlw-vaccine.svg', bbox_inches="tight")
