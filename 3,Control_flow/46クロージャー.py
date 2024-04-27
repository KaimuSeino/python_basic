def outer(a, b):

  def inner():
    return a + b
  
  return inner

print(outer(1, 2))

f = outer(1, 2)
r = f()
print(r)

# クロージャーの使い所
# 円の面積を求める場合...
def circle_area_func(pi):
  def circle_area(radius):
    return pi * radius * radius
  
  return circle_area

# piを3.14で計算したいとき
cal1 = circle_area_func(3.14)

# piを3.1415926535で計算したいとき
cal2 = circle_area_func(3.1415926535)

print(cal1(7))
print(cal2(7))

# 初めに設定した引数を用途によって使い分けたいときに使う！！！