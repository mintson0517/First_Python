import random as r
for i in range(0,5):
    print(r.randint(1,100), end=",")
    print(r.randrange(0,12,2), end=",")#2ずつ増加する(ランダム)
    print(r.random())
    print(r.uniform(3,10))#3-10の間にある数字をランダムで出力