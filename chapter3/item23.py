# キーワード引数にオプションの振る舞いを与える

def print_parameters(param1, *args, **kwargs):
    # 通常の引数
    print(f"param1: {param1}")
    # argsは可変長引数。配列など。
    print(f"args: {args}")
    # kwargsはキーワード引数。辞書。
    for key, val in kwargs.items():
        print(f"{key}: {val}")


kv_list = ["a", "b", "c"]
# alpha, beta, gammaなどは自由に定義することが可能となります。
# kv_listの「*」を除外すると、kv_listが一つの要素と解釈され、args: (['a', 'b', 'c'],)と出力されるため注意。
print_parameters(1, *kv_list, alpha=1, beta=2, gamma=3)
"""
param1: 1
args: ('a', 'b', 'c')
alpha: 1
beta: 2
gamma: 3
"""

kv_list = ["a", "b", "c"]
kv_dct = {"alpha": 1, "beta": 2, "gamma": 3}
# 「**辞書」の形で引数に取ることも可能です。
print_parameters(1, *kv_list, **kv_dct)
"""
param1: 1
args: ('a', 'b', 'c')
alpha: 1
beta: 2
gamma: 3
"""
