# ninenine
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print("%d*%d=%2d  " % (i, j, product), end="")
    print()

# break(ループを終了させる)
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=",")
