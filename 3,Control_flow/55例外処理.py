l = [1, 2, 3]
i = 5

try:
  print(l)
except IndexError as ex:
  print("インデックスエラーが発生しています。 {}".format(ex))
except NameError as e:
  print("ネームエラーが発生しています。 {}".format(e))
except Exception as e:
  print("何か問題が起きました。 {}".format(e))
else:
  print("tryが成功した時に出力される!")
finally:
  print("ファイナリー")
