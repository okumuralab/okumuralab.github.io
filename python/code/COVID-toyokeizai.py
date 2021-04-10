# wget -N https://toyokeizai.net/sp/visual/tko/covid19/data/data.json

import json
import numpy as np
import matplotlib.pyplot as plt

with open("data.json") as f:
    data = json.load(f)

def foo(x, depth=0):
    if type(x) == dict:
        for i in x.keys():
            print(" " * 4 * depth, i, sep="")
            foo(x[i], depth + 1)

# foo(data)

# data["updated"]["last"]["ja"]  # => '最終更新：2021年4月9日'
# data["updated"]["demography"]["ja"]  # => '4月7日時点'

# 'carriers', 'pcrtested', 'discharged', 'serious', 'deaths', 'reproduction'
# 検査陽性者数 PCR検査人数 退院者数 重症者数 死亡者数 実効再生産数

carriers = np.array(
    [np.sum(data["prefectures-data"][i]["carriers"]["values"]) for i in range(47)]
)
deaths = np.array(
    [np.sum(data["prefectures-data"][i]["deaths"]["values"]) for i in range(47)]
)

# 2019-10-01人口（1000人）

population = np.array([5250, 1246, 1227, 2306, 966, 1078, 1846,
     2860, 1934, 1942, 7350, 6259, 13921, 9198, 2223, 1044, 1138, 768,
     811, 2049, 1987, 3644, 7552, 1781, 1414, 2583, 8809, 5466, 1330,
     925, 556, 674, 1890, 2804, 1358, 728, 956, 1339, 698, 5104, 815,
     1327, 1748, 1135, 1073, 1602, 1453])

kenmei = ["北海道", "青森", "岩手", "宮城", "秋田", "山形", "福島",
          "茨城", "栃木", "群馬", "埼玉", "千葉", "東京", "神奈川",
          "新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜",
          "静岡", "愛知", "三重", "滋賀", "京都", "大阪", "兵庫",
          "奈良", "和歌山", "鳥取", "島根", "岡山", "広島", "山口",
          "徳島", "香川", "愛媛", "高知", "福岡", "佐賀", "長崎",
          "熊本", "大分", "宮崎", "鹿児島", "沖縄"]

plt.scatter(carriers, deaths)
for x, y, s in zip(carriers, deaths, kenmei):
    plt.text(x, y, s)
plt.xlabel("感染者数")
plt.ylabel("死者数")
plt.figtext(0.9, 0.89,
            data["updated"]["last"]["ja"] + " " + data["updated"]["demography"]["ja"],
            horizontalalignment='right')
plt.savefig("../img/COVID-toyokeizai-1.svg", bbox_inches="tight")

plt.clf()
plt.scatter(carriers / population, deaths / population)
for x, y, s in zip(carriers / population, deaths / population, kenmei):
    plt.text(x, y, s)
plt.xlabel("人口1000人あたり感染者数")
plt.ylabel("人口1000人あたり死者数")
plt.figtext(0.9, 0.89,
            data["updated"]["last"]["ja"] + " " + data["updated"]["demography"]["ja"],
            horizontalalignment='right')
plt.savefig("../img/COVID-toyokeizai-2.svg", bbox_inches="tight")
