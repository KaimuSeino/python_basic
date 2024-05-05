shuffle_num = 4

def cards_shuffle(cards_array):
  cardsLen = len(cards_array)
  split_index = cardsLen // 2

  first_half = cards_array[:split_index]
  second_half = cards_array[split_index:]

  result_array = []

  for first_card, second_card in zip(first_half, second_half):
    result_array.append(first_card)
    result_array.append(second_card)
  
  return result_array

cards = []

for design in ["S", "H", "D", "C"]:
  for i in range(1, 14):
    cards.append(f"{design}_{i}")

for _ in range(shuffle_num):
  cards = cards_shuffle(cards)

for card in cards:
  print(card)