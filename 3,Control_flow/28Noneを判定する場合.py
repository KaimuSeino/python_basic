is_empty = "" # javascriptでいう null

# None を判別するためにisを使う

print(type(is_empty))

if is_empty is not None:
  print("True")
else:
  print("False")
