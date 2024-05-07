X = 10
F1, F2 = 7, 3
L, N = 100, 1
stops = [50]

total_fuel = 0
current_position = 0

for next_stop in stops + [L]:
  segment_length = next_stop - current_position

  # Xメートルまでの燃費計算
  if segment_length <= X:
    total_fuel += segment_length * F1
  else:
    total_fuel += X * F1 + (segment_length - X) * F2

    current_position = next_stop


print(total_fuel)