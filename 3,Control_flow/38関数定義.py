def hello_func():
  return "hello"

print(type(hello_func))

func = hello_func()

print(func)

def what_your_name(name):
  if name == "kaimu":
    print(name, "seino")
  elif name == "kosei":
    print(name, "suzuki")
  else:
    print("誰その人？？")


what_your_name("kosei")
