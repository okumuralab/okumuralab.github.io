import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.proportion import proportion_confint

df = pd.read_excel("https://oku.edu.mie-u.ac.jp/~okumura/stat/data/abo.xlsx")

kenmei = ["北海道", "青森", "岩手", "宮城", "秋田", "山形", "福島", "茨城",
          "栃木", "群馬", "埼玉", "千葉", "東京", "神奈川", "新潟", "富山",
          "石川", "福井", "山梨", "長野", "岐阜", "静岡", "愛知", "三重",
          "滋賀", "京都", "大阪", "兵庫", "奈良", "和歌山", "鳥取", "島根",
          "岡山", "広島", "山口", "徳島", "香川", "愛媛", "高知", "福岡",
          "佐賀", "長崎", "熊本", "大分", "宮崎", "鹿児島", "沖縄"]
pref = pd.DataFrame({"id": range(1,48), "都道府県名": kenmei})

df2 = pd.read_excel("https://oku.edu.mie-u.ac.jp/~okumura/stat/data/abo2010.xlsx")
df2 = pd.merge(pref, df2, on="都道府県名")

n1 = np.round(df[["O型","A型","B型","AB型"]].iloc[49] / 100 * df['検査人員'][49])
n2 = df2[["計O","計A","計B","計AB"]].sum(axis=0)
n3 = [89326, 102229, 67376, 38469]
n4 = [253, 297, 197, 123]
n5 = [167791, 186333, 116163, 67069]

def prop(n):
    n = np.array(n)
    ntot = sum(n)
    p = n / ntot
    ci0, ci1 = proportion_confint(n, ntot, method='beta') # Clopper-Pearson
    return p, np.array([p - ci0, ci1 - p])

x = np.array([1,2,3,4])
plt.clf()

p, ci = prop(n1)
plt.errorbar(x, p, ci, fmt="o", label='古畑')

p, ci = prop(n2)
plt.errorbar(x+0.1, p, ci, fmt="o", capsize=5, label='高校生')

p, ci = prop(n3)
plt.errorbar(x+0.2, p, ci, fmt="o", capsize=5, label='@rocinate__')

p, ci = prop(n4)
plt.errorbar(x+0.3, p, ci, fmt="o", capsize=5, label='@dempacat')

p, ci = prop(n5)
plt.errorbar(x+0.4, p, ci, fmt="o", capsize=5, label='@fukada0318')

plt.xticks(x+0.2, ["O","A","B","AB"])
plt.legend()
plt.savefig('../img/abo4.svg', bbox_inches="tight")
