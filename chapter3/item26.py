# 26：functools.wrapを使って関数デコレータを定義する

from functools import wraps

# ラッパー関数の書き方は以下
# 1. 引数はラップしたい関数(f)を取る
# 2. その中で何らかの関数wrapper(*args, **kwargs)を定義し、その上に@wraps(f)と記述
# 3. wrapperはfを実行し、結果をreturnすることに加えて行いたい処理を記述（ここでは関数名や引数のprint）
# 4. ラッパー全体としては中で定義した関数をreturn
def print_funcname(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"関数 {f.__name__} が呼び出されました。")
        print(f"位置引数は {args} です。")
        print(f"キーワード引数は {kwargs} です。")
        result = f(*args, **kwargs)
        return result
    return wrapper


# hoge関数の直前に@fugaと書くと、ただのhogeではなくfuga(hoge)を実行したことになります。
# この例ではprint_funcname(main)
@print_funcname
def main(a, b):
    print(a, b)


main(1, b=2)
"""
関数 main が呼び出されました。
位置引数は (1,) です。
キーワード引数は {'b': 2} です。
1 2
"""


# 補足1：これが役に立つ例
# 再帰関数のデバッグ

def trace(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f"{f.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper

@trace
def fib(n: int) -> int:
    """フィボナッチ数列の計算

    Args:
        n (int): 第何項を求めるか

    Returns:
        int: フィボナッチ数列の求めたい項
    """
    if n in (0, 1):
        return n
    return fib(n-2) + fib(n-1)

# 関数の呼び出し状況をトレースすることができる。
# 1. n=3でfib(n)を求めたい。
#   i.  fib(n-2)が呼ばれてfib(1)=1
#   ii. fib(n-1)が呼ばれて、fib(2)を求めたい
#       a. まずn=2でfib(n-2)が呼ばれて、fib(0)=0
#       b. 次にn=2でfib(n-1)が呼ばれてfib(1)=1
#       c.これらを合わせてfib(2)=1
#   iii.これらを合わせてfib(3)=3
fib(3)
"""
fib((1,), {}) -> 1
fib((0,), {}) -> 0
fib((1,), {}) -> 1
fib((2,), {}) -> 1
fib((3,), {}) -> 2
"""


# 補足2:functools.wrapの意義
# @wraps(f)をつけておかないと、以下の出力が「wrapper」になってしまう。
# より高度なプログラムを書くにあたっては、これが問題になることがある(その8の発表をお楽しみに)
print(fib.__name__)
"""
fib
"""
