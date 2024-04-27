# some_list = [1, 2, 3, 4, 5]

# i = 0

# while i < len(some_list):
#   print(f"リスト{i} =", some_list[i])
#   i += 1

# for i in some_list:
#   print("some_listの中身 =", i)

index = 0

for s in "abcdefg":
  print(f"abcdefg[{index}] =", s)
  index += 1


for word in ["a", "b", "c", "d", "e"]:
  if word == "c":
    continue

  print(word)


