list = ["おはよう", "こんにちは", "さようなら"]

for i in list:
  print(i)

print("##################")

def counter(num=10):
  for _ in range(num):
    yield "Run!!!"

# 処理を小分けにすることで、パフォーマンスを向上させる
def greeting():
  yield "おはよう"
  #めっちゃ重たい処理
  yield "こんにちは"
  #めっちゃ重たい処理
  yield "さようなら"

# for g in greeting():
#   print(g)

g = greeting()
c = counter()
print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))