n = int(input("正の整数を入力してください"))
for i in range(1, n + 1):
    if i % 5 == 0:
        continue
    print(i, end=" ")
