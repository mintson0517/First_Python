def ctof(c):
    f = c * 1.8 + 32
    return f


inputc = float(input("摂氏（℃）を入力してください"))
print("華氏の温度：%5.1f ℉" % ctof(inputc))