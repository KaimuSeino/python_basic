# def say_something(word, word2, word3):
#   print(word)
#   print(word2)
#   print(word3)

# say_something("HI!", "Kaimu", "Seino")

def say_something_args(word, *args):
  print("word =", word)
  for arg in args:
    print(arg)
  print(args)

say_something_args("Hi", "My", "Name", "is", "Kaimu")