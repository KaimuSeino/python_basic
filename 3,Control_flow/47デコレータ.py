def print_info(func):
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return wrapper

def print_more(func):
  def wrapper(*args, **kwargs):
    print("func:", func.__name__)
    print("args:", args)
    print("kwargs:", kwargs)
    result = func(*args, **kwargs)
    print("result:", result)
    return result
  return wrapper

# これは？？？？
# @print_info
# @print_more
def add_num(a, b):
  return a + b

# r = add_num(30, 40)
# print(r)


# add_numをprint_moreで包んで、さらに、print_moreをprint_infoで包み込む
f = print_info(print_more(add_num))
r = f(20, 70)
print(r)