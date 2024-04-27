animal = "dog" # こいつはグローバル変数


def func():
  """\
  ドキュメント\
  """
  # global animal
  # print("グローバル動物", animal)
  # animal = "cat"
  # print("funcの動物", animal)
  # a = "a"
  # print(locals())
  print(func.__name__)
  print(func.__doc__)

print("どっちだ？", animal)

func()

# print(globals())
print("global", __name__)
