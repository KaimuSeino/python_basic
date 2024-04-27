def test_func(x, l = []): # デフォルト引数で[]や{}を入れるとアドレス参照などでバグになりやすい
  l.append(x)
  return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

def test01_func(z, list = None):
  if list is None:
    list = []
  list.append(z)
  return list

result = test01_func(100)
result = test01_func(100)
print(result)