from typing import List
from collections import Counter, OrderedDict
import sys


# title 3; contents 1
titles = Counter()
kws_all = Counter()
# 多行输入
(top_k, counts) = [int(v) for v in sys.stdin.readline().split()]
max_kw = [0] * top_k
for i in range(counts):
    tmp_title: list = sys.stdin.readline().split()
    tmp_contents = sys.stdin.readline().split()
    for kw in tmp_title:
        titles[kw] += 1
        kws_all[kw] += 3
    for kw in tmp_contents:
        kws_all[kw] += 1
# order
print(titles)
print(kws_all)
candidates = list(kws_all.keys())
candidates.sort(key=lambda kw: -kws_all[kw])
res: List[str] = []
c = 0
for i in range(top_k):
    if kws_all[candidates[c]] > kws_all[candidates[c+1]]:
        v = candidates.pop(c)
    elif titles[candidates[c]] > titles[candidates[c+1]]:
        v = candidates.pop(c)
    else:
        v = candidates.pop(c+1)
        c -= 1
    res.append(v)
    c += 1
print(res)
