# ユーグリッドの法則を使用
print("最小公倍数を求めます")
a = int(input("aの数値を入力してください："))
b = int(input("bの数値を入力してください："))


# aとbの最大公約数を求める関数
def gcd(x, y):  # def(define定義する)
    while y != 0:
        (x, y) = (y, x % y)
    return x


# aとbの最小公倍数を計算
lcm = (a * b) // gcd(a, b)

print("%dと%dの最小公倍数は%dです" % (a, b, lcm))
