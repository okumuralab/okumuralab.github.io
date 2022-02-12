#! /usr/local/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

URL = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/vaccine_sesshujisseki.html"
df = pd.read_html(URL, header=0)[0]

t = pd.to_datetime(df['日付'][:-1])
n1 = df['内１回目'][:-1]
n2 = df['内２回目'][:-1]

plt.bar(t, n1, label="1st")
plt.bar(t, n2, bottom=n1, label="2nd")
plt.legend()
plt.xticks(rotation=20)

plt.savefig("../img/mhlw-vaccine.svg", bbox_inches="tight")
