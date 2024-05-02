"""
マップの行数 H と列数 W とナンバリングの向き D が与えられる、
(0, 0) から指示通りにナンバリングしたとき、マップ全体にどのように番号が振られるかを出力する。

D = 1の場合

1  3  6  9
2  5  8 11
4  7 10 12

D = 2の場合

1  2  3  4
5  6  7  8
9 10 11 12

D = 3の場合

1  4  7 10
2  5  8 11
3  6  9 12

D = 4の場合

1  2  4  7
3  5  8 10
6  9 11 12
"""

# 一番最初につまづくところは 二次元配列をどうやって作っていくかがわからなかった。

# def d_1(h, w):
#   # D = 1
#   # ここで[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]を作成
#   result = [[0] * w for _ in range(h)]
#   num = 1
#   for s in range(w + h - 1):
#     for x in range(w):
#       y = s - x
#       if 0 <= y < h:
#         result[y][x] = num
#         num += 1

#   return result
  

# for row in d_1(2, 2):
#   print(" ".join(map(str, row)))

# print("######################")

# def d_2(h, w):
#   # D = 2
#   result = [[0] * w for _ in range(h)]
#   num = 1
#   for y in range(h):
#     for x in range(w):
#       if 0 <= x < w:
#         result[y][x] = num
#         num += 1
  
#   return result

# for row in d_2(4, 4):
#   print(" ".join(map(str, row)))

# print("##############################")

# def d_3(h, w):
#   # D = 3
#   result = [[0] * w for _ in range(h)]
#   num = 1
#   for x in range(w):
#     for y in range(h):
#       if 0 <= y < h:
#         result[y][x] = num
#         num += 1
  
#   return result

# for row in d_3(4, 4):
#   print(" ".join(map(str, row)))

# print("##############################")

def d_4(h, w):
  # D = 4
  result = [[0] * w for _ in range(h)]
  num = 1
  for s in range(h + w - 1):
    for y in range(h):
      x = s - y
      if 0 <= x < w:
        result[y][x] = num
        num += 1
  
  return result


for row in d_4(4, 8):
  print(" ".join(map(str, row)))


# def fill_d(h, w, d):
#   result = [[0] * w for _ in range(h)]
#   num = 1

#   if d == 1:
#     for s in range(w + h - 1):
#       for x in range(w):
#         y = s - x
#         if 0 <= y < h:
#           result[y][x] = num
#           num += 1
#     return result
  
#   if d == 2:
#     for y in range(h):
#       for x in range(w):
#         if 0 <= x < w:
#           result[y][x] = num
#           num += 1
#     return result
  
#   if d == 3:
#     for x in range(w):
#       for y in range(h):
#         if 0 <= y < h:
#           result[y][x] = num
#           num += 1
#     return result
  
#   if d == 4:
#     for s in range(h + w - 1):
#       for y in range(h):
#         x = s - y
#         if 0 <= x < w:
#           result[y][x] = num
#           num += 1
#     return result
