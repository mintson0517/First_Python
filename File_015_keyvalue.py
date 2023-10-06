dict1 = {"金メダル": 26, "銀メダル": 34, "銅メダル": 30}
listkey = list(dict1.keys())  # word
listvalue = list(dict1.values())  # number
for i in range(len(listkey)):
    print("%s枚の%dを獲得しました" % (listkey[i], listvalue[i]))
