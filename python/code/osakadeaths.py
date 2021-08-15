import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/osakadeaths.csv')

def days(year, month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1] + ((month == 2) and
                           ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)))

perday = np.array([r[2] / days(r[0], r[1]) for i, r in df.iterrows()])

plt.clf()
for y in range(2015, 2022):
    plt.plot(df[df['year'] == y]['month'], perday[df['year'] == y], 'o-', label=y)

plt.legend()
plt.savefig('../img/osakadeaths.svg', bbox_inches="tight")

plt.clf()
for m in range(1, 13):
    plt.plot(df[df['month'] == m]['year'], perday[df['month'] == m],
             marker=f'${m}$', label=str(m)+'月')
# plt.legend()
plt.savefig('../img/osakadeaths1.svg', bbox_inches="tight")

