import random as r

list1 = r.sample(range(1, 50), 7)
special = list1.pop()
list1.sort()

print("今回の当選番号は：", end="")
for i in range(0, 6):
    if i == 5:
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=", ")

print("特別当選番号は：" + str(special))
