#! /usr/bin/env python3

import japanmap as jp
import matplotlib.pyplot as plt
import numpy as np

def pref_map1(ips, cols=None, texts=None, width=1, qpqo=None, rough=False, tostr=False, ratio=(0.812, -1)):
    """ベクトルデータ(SVG)"""
    from IPython.display import SVG
    assert all(1 <= ip <= 47 for ip in ips), 'Must be 1 <= ip <= 47'
    if cols is None:
        cols = 'red fuchsia purple navy blue teal aqua green ' \
               'lime olive yellow orange orangered maroon'.split()
    elif isinstance(cols, str) and cols == 'gray':
        cols = ['#%02x%02x%02x' % ((i * 18 + 32,) * 3) for i in [1, 8, 5, 10, 3, 0, 4, 7, 2, 9, 6]]
    if texts is None:
        texts = [''] * len(ips)
    pnts = jp.pref_points(qpqo, rough)
    pp = [[[i[0] * ratio[0], i[1] * ratio[1]] for i in pnts[ip - 1]] for ip in ips]
    ppp = np.array(sum(pp, []))
    mx, mn = np.nanmax(ppp, 0), np.nanmin(ppp, 0)
    mx = max(mx - mn)
    s = ''.join('<path fill="none" stroke="gray" stroke-width="0.001" d="%s"/>' %
                ('M' + ' '.join(['L%g,%g' % (x, y) for x, y in (p - mn) / mx])[1:] + ' Z')
                for i, p in enumerate(pp))
    c = list((np.mean([(x, y) for x, y in (p - mn) / mx], axis=0) for i, p in enumerate(pp)))
    t = ''.join('<text x="%g" y="%g" text-anchor="middle">%s</text>' % (c[i][0], c[i][1], texts[i]) for i in range(len(ips)) if texts[i] != '')
    s = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="400" height="400" viewBox="0 0 %d 1" style="font-family:sans-serif; font-size:0.04">%s%s</svg>' % (width, s, t)
    return s if tostr else SVG(s)

data = {
    '北海道': 16,
    '青森県': 0,
    '岩手県': 0,
    '宮城県': 0,
    '秋田県': 0,
    '山形県': 0,
    '福島県': 0,
    '茨城県': 0,
    '栃木県': 0,
    '群馬県': 0,
    '埼玉県': 1,
    '千葉県': 8,
    '東京都': 28,
    '神奈川県': 12,
    '新潟県': 0,
    '富山県': 0,
    '石川県': 1,
    '福井県': 0,
    '山梨県': 0,
    '長野県': 0,
    '岐阜県': 0,
    '静岡県': 0,
    '愛知県': 11,
    '三重県': 1,
    '滋賀県': 0,
    '京都府': 2,
    '大阪府': 1,
    '兵庫県': 0,
    '奈良県': 1,
    '和歌山県': 13,
    '鳥取県': 0,
    '島根県': 0,
    '岡山県': 0,
    '広島県': 0,
    '山口県': 0,
    '徳島県': 0,
    '香川県': 0,
    '愛媛県': 0,
    '高知県': 0,
    '福岡県': 2,
    '佐賀県': 0,
    '長崎県': 0,
    '熊本県': 3,
    '大分県': 0,
    '宮崎県': 0,
    '鹿児島県': 0,
    '沖縄県': 3
}

def foo(x):
    if x == 0:
        return ''
    else:
        return str(x)

t = [foo(x) for x in data.values()]

s = pref_map1(range(1,48), texts=t, tostr=True)
with open("../img/COVID-map.svg", "w") as f:
    f.write(s)
