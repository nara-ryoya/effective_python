from typing import Dict, MutableMapping
import json


def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


class SortedDict(MutableMapping):
    """難しそうなことをしているが、要するに英字順で出てくるような辞書を自分で作ってあげようということ"""

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return json.dumps(self.data)


votes: Dict[str, int] = {"otter": 1281, "polar_bear": 587, "fox": 863}

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)
