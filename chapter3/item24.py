# 動的なデフォルト引数を指定するときはNoneとdcostringを使う

import json
from typing import Optional

# NG例。デフォルト引数は、関数が定義された瞬間にしか評価されない。
def decode(path, default={}):
    try:
        return json.loads(path)
    except ValueError:
        return default

# 実行を繰り返すと同じ辞書オブジェクトに追加されていくという不思議な状況が発生する。
foo = decode("not a valid path")
foo["x"] = 1
bar = decode("bad path again")
bar["y"] = 2
print(foo)
print(bar)
"""
{'x': 1, 'y': 2}
{'x': 1, 'y': 2}
"""

# OK例。重要なことは以下の2点
# 1. Noneをデフォルト値にすること
# 2. その代わりに、関数の中での実際の振る舞いをdocstringに記述すること
def decode2(path: str, default: Optional[dict]=None):
    """jsonをdictとして読み込む。

    Args:
        path (str): jsonのパス
        default (Optional[dict], optional): loadに失敗した際の返り値。デフォルトは空のdict。

    Returns:
        dict: jsonを読み込んだもの
    """
    try:
        return json.loads(path)
    except ValueError:
        if default is None:
            default = {}
        return default

# 直感に合う動作をする。
foo = decode2("not a valid path")
foo["x"] = 1
bar = decode2("bad path again")
bar["y"] = 2
print(foo)
print(bar)
"""
{'x': 1}
{'y': 2}
"""

"""md

参考：

[vscodeの拡張機能autoDocstringを用いて自動生成できる](https://bluebirdofoz.hatenablog.com/entry/2019/12/05/092551)

[色々なdocstring](https://qiita.com/flcn-x/items/393c6f1f1e1e5abec906)

"""
