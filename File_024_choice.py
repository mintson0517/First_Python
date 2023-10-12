import random as r

for i in range(0, 9):
    print(r.choice("HelloWorld"), end=",")
    print(r.choice([1,2,3,4,5,6,7,8,9,10]),end=",")