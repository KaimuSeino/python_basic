# def user(**kwargs):
#   for k, v in kwargs.items():
#     print(f"{k}: {v}")


# d = {
#   "user": "kaimu",
#   "email": "kaimuSeino@gmail.com",
#   "pwd": "pwd"
# }

# user(**d)

def menu(food, *args, **kwargs):
  print(food)
  print(args)
  print(kwargs)

menu("banana", "apple", "orange", name="kaimu", pwd="pwd")

