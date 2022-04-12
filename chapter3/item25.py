# 25：キーワード引数・位置引数の明確さを高める


# 時間帯と性別に応じて変化する挨拶文を作成する関数
def greeting(firstname, lastname, eos, is_night, is_male):
        greet = "Good Evening" if is_night else "Hello"
        title = "Mr." if is_male else "Ms."
        print(f"{greet}, {title} {firstname} {lastname} {eos}")


# 2つのTrueが、それぞ時間帯・性別どちらに対するboolなのかがここだけ見るとわかりません。
greeting("Kazuki", "Egashira", "!!!", True, True)
"""
Good Evening, Mr. Kazuki Egashira !!!
"""

# 改善点は2点
# 1. 「/」を使うことで、これよりも前は位置引数としてしか使えなくなった。(PYTHON3.8以降なので注意)
#   これにより「関数をリファクタして変数名を「myoji」「namae」にしたせいで関数が動かなくなった！」などになりづらい
# 2. 「*」を使うことで、これよりも後はキーワード引数として使えなくなった。
#   これにより関数が使用されているコードを見た際に「このTrueどっちの意味だろう？」などになりづらい

def greeting_better(firstname, lastname, /, eos, *, is_night=False, is_male=False):
        greet = "Good Evening" if is_night else "Hello"
        title = "Mr." if is_male else "Ms."
        print(f"{greet}, {title} {firstname} {lastname} {eos}")

# greeting_better(firstname="Kazuki", lastname="Egashira", "!!!", is_night=True, is_male=True)  # Error
# greeting_better("Kazuki", "Egashira", "!!!", True, True)  # Error
greeting_better("Kazuki", "Egashira", "!!!", is_night=True, is_male=True)

"""
Good Evening, Mr. Kazuki Egashira !!!
"""
