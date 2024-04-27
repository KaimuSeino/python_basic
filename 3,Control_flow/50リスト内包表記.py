t = (1, 2, 3, 4, 5)

r = []
for i in t:
  if i % 2 == 0:
    r.append(i)

print(r)

print("リスト内包表記は上記を一発でかける")

list = [i for i in t if i % 2 == 0]
print(list)

print("\n#############################")

t2 = (6, 7, 8, 9, 10)

r = []
list = []
for i in t:
  for j in t2:
    r.append(i * j)

list = [i * j for i in t for j in t2] # こっちの方がわかりずれー

print("r", r)
print(len(r))
print("list", list)