innum = 0
list1 = []
while innum != -1:
    innum = int(input("電気代を入力してください（-1：終了）"))
    list1.append(innum)
list1.pop()
print("合計で%dか月の電気代が入力されました" % len(list1))
print("最大の電気代は：%d" % max(list1))
print("最小の電気代：%d" % min(list1))
print("総合の電気代：%d" % sum(list1))
print("電気代を最大から最小に並べなおす：{}".format(sorted(list1, reverse=True)))
