# from kaimu_package.talk import animal
# from kaimu_package.talk import human

from kaimu_package.talk import * # animalとhumanをまとめてインポート
# *を読み込むと talkの__init__ファイルが読み込まれる。__all__の配列の部分を編集するとanimalやhumanが使える。
# けどあんまり使わない方がいいです

print(animal.sing())
print(animal.cry())