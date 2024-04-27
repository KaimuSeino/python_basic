list = ["mon", "tue", "wed", "Thu", "fri", "sat", "sun"]

def change_words(words, func):
  for word in words:
    print(func(word))


# def capitalize_func(word):
#   return word.capitalize()

#↑をラムダで一行でかけるみたい
capitalize_func = lambda word: word.capitalize()

change_words(list, capitalize_func)