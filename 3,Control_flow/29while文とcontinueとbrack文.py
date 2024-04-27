# count = 0

# while count < 5:
#   print("カウント =", count)
#   count += 1


count1 = 0

while True:
  if count1 >= 5:
      break
  
  if count1 == 2:
     count1 += 1
     print("カウントが２のときに飛ばすぜ！！！")
     continue
  
  print("カウント1 =", count1)
  count1 += 1