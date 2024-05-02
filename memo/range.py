# for i in range(1, 3): # iには1, 2が入る
#   print(i)


height, width = 3, 3
y, x = 0, 0
boardSurface = [
  ['.', '#', '.'],
  ['.', '#', '#'],
  ['#', '.', '.'],
]

"""
boardSurface
3 3
##.
###
...
0 0

与えられた座標のマス(y, x) と、 (y, x) と同じ縦・横・斜めの列に存在する全てのマスについて
マスに書かれている文字が "." の場合は "#" に、"#" の場合は "." に書き換える。
"""

# 縦列の処理
for i in range(height):
  if boardSurface[i][x] == ".":
    boardSurface[i][x] = "#"
  else:
    boardSurface[i][x] = "."

#横列の処理
for j in range(width):
  if boardSurface[y][i] == ".":
    boardSurface[y][i] = "#"
  else:
    boardSurface[y][i] = "."

for k in range(1, min(height, width)):
  # y = -x 方向の処理
  if y + k < height and x + k < width:
    if boardSurface[y + k][x + k] == ".":
      boardSurface[y + k][x + k] = "#"
    else:
      boardSurface[y + k][x + k] = "."

  if y - k >= 0 and x - k >= 0:
    if boardSurface[y - k][x - k] == ".":
      boardSurface[y - k][x - k] = "#"
    else:
      boardSurface[y - k][x - k] = "."
  
  # y = x 方向の処理
  if y - k >= 0 and x + k < width:
    if boardSurface[y - k][x + k] == ".":
      boardSurface[y - k][x + k] = "#"
    else:
      boardSurface[y - k][x + k] = "."

  if y + k < height and x - k >= 0:
    if boardSurface[y + k][x - k] == ".":
      boardSurface[y + k][x - k] = "#"
    else:
      boardSurface[y + k][x - k] = "."

# 中心座標の処理
if boardSurface[y][x] == ".":
  boardSurface[y][x] = "#"
else:
  boardSurface[y][x] = "."

# 値の出力
for row in boardSurface:
  print("".join(row))


  


