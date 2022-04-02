# 13:atch-allアンパック

a = [1, 2, 3, 4, 5]

# NG例。off-by-oneエラー(境界条件に関するエラー)を誘発しうる
# 例えば「境界値を1ヶ所修正し忘れた」とかが起こりうる
first = a[0]
second = a[1]
others = a[2:]
print(first, second, others)

# OK例。「*hoge」で「それ以外全部」を受け取れる(=catch-all unpack)
first, second, *others = a
print(first, second, others)

# *hogeに入れるものがない場合は空のリストになる。
# 「少なくともN個ある」とわかっている処理で使えそう
b = [1, 2]
first, second, *others = b
print(first, second, others)
