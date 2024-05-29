import builtins # 実際はこれ

builtins.print("こんにちは！")

print() # こういうのが組み込み関数

# print(globals())

ranking = {
  "A": 100,
  "B": 80,
  "C": 90,
}

for key in ranking:
  print(key)

print(sorted(ranking, key=ranking.get, reverse=True))


