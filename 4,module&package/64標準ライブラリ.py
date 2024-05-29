# 標準ライブラリ
# https://docs.python.org/ja/3/library/

# とりあえず代表的なやつをやろう


s = "jsfoaonfbewfjapsafoouheiwfgbanckmpoqwhfigqwknqppmmznjkjcbibjsbhsibdaufe"

d = {}
for c in s:
  if c not in d:
    d[c] = 0
  d[c] += 1

print(d)

d = {}
for c in s:
  d.setdefault(c, 0)
  d[c] += 1

print("setdefault:",d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
  d[c] += 1

print(d)
print(d["f"])