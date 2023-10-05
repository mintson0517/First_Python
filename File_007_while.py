total = i = 1
print("Nの階乗を計算いたします")
n = int(input("正の整数を入力してください："))
while i <= n:
    total *= i
    i += 1
print("%d!=%d" % (n, total))
