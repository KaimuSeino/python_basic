# # raise IndexError("インデックスエラーだぞ！気をつけたまえ！")

# class UppercaseError(Exception):
#   pass

# def check():
#   words = ["APPLE", "orange", "banana"]
#   for word in words:
#     if word.isupper():
#       raise UppercaseError(word)

# try:

#   check()

# except UppercaseError as ex:
#   print("This is my error")

n = 10
if n <= 10:
  print("low")
else:
  print(n)