count = 0

while count < 5:
  print("カウント =", count)
  count += 1
else:
  print("終了しました")


break_count = 0

while break_count < 5:

  if break_count == 2:
    break

  print("ブレイクカウント =", break_count)
  break_count += 1

else:
  print("終了しました")