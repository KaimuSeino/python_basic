try:
  from kaimu_package import utils
except ImportError: # バージョンが古い時でも新しい時でも使えるようにする
  from kaimu_package.tools import utils


utils.say_twice("kaimu")