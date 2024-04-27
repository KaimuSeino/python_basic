def example_func(param):
  """
  Example functionです。
  ここにはparam: int が引数として設定されています。

  returnはbool型が帰ってきます。
  
  """

  print(param)
  print("doc")

  return True

print(example_func.__doc__)