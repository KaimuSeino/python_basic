single_attack_power = 7
overall_attack_power = 3

monster_list = {
  "スライム": 24,
  "ゴーレム": 45,
  "スライムナイト": 35,
  "ドラキー": 29
}

min_attack_num = 0 #初期値0

"""
「単体攻撃」と「全体攻撃」をどのように組み合わせれば、最速でモンスタを倒すことができるかを考える
"""

# モンスター全てのHPをリストに格納する
monster_hp_list = list(monster_list.values())
print("グローバルなモンスターのHPリスト", monster_hp_list)

def overall_attack_func(hp_list):
  # 全体攻撃をした後のモンスターのHPを表示する。
  attacked_hp_list = []
  for hp in hp_list:
    # 全体攻撃を受けたモンスターのhp
    overall_attacked_hp = hp - overall_attack_power
    print("ダメージを受けたHP", overall_attacked_hp)
    # もし0以下になった場合は0をリストに格納する。
    attacked_hp_list.append(max(0, overall_attacked_hp))
  
  return attacked_hp_list

def single_attack_func(hp_list):
  # 単体攻撃はHPの一番高いモンスターに対して行う
  monster_max_hp = max(hp_list)
  index = hp_list.index(monster_max_hp)
  hp_list[index] -= single_attack_power
  print(f"{index}のモンスターのHP", hp_list[index])

  return hp_list


