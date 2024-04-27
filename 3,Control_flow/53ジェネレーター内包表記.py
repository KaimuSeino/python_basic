def generator():
  for i in range(10):
    yield i

g = generator()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

generator2 = (i for i in range(10) if i % 2 == 0)

for x in generator2:
  print(x)