# import kaimu_package.utils as kaimu
from kaimu_package import utils as ut
from kaimu_package.talk import human as hu



result = ut.say_twice("Hello")

cry = hu.cry()
sing = hu.sing()

print(cry, sing)

print(result)