# 数列変数　=　range(開始,最後,間隔値)
list1 = range(10)
list2 = range(1, 10)
list3 = range(1, 10, 2)
list4 = range(10, 1, -2)
print(list(list1))
print(list(list2))
print(list(list3))
print(list(list4))

# for
for n in range(3):
    print(n, end=",")

n = int(input("正の整数を一つ入力してください"))
for i in range(1, n + 1):
    print(i, end=" ")

# sum
sum = 0
n = int(input("正の整数を入力してください："))
for i in range(1, n + 1):
    sum += i

# ループの外で合計を表示
print("1から{}までの正の整数の和は{}です".format(n, sum))
