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
