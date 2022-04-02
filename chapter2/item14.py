# 14:複雑な基準でソートする

from dataclasses import dataclass

@dataclass
class Genius:
    name: str
    hensachi: float
    def __repr__(self) -> str:
        """print時の挙動定義"""
        return f"Genius({self.name}, {self.hensachi})"

geniuses = [
    Genius("nara", 100.0),
    Genius("egashira", 89.5),
    Genius("gonokami", 10.0)
]
# 通常のsortではTypeError: '<' not supported between instances of 'Genius' and 'Genius'
# keyを指定することで、str同士、float同士の大小比較にすることが可能。
geniuses.sort(key=lambda x: x.name)
print(geniuses)
geniuses.sort(key=lambda x: x.hensachi)
print(geniuses)



tup_list = [("apple", 20), ("cherry", 30), ("banana", 10), ("cherry", 20)]

# アルファベット順に並べる
tup_list.sort(key=lambda x: x[0], reverse=True)
print(tup_list)
# 数が大きい方から並べ、同一のものがあればアルファベットの逆順に並べる
tup_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(tup_list)
# 数字が大きい方から並べ、同一のものがあればアルファベット順に並べる
# 数字はマイナスにすることで並び方が逆順になることを利用。
tup_list.sort(key=lambda x: (-x[1], x[0]))
print(tup_list)
