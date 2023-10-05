scores = []
total = inscore = 0
print("学生の成績総合や平均を求めます（入力しない場合は”-1”を記入")
while (inscore != -1):
    inscore = int(input("学生の成績を入力してください："))
    if(inscore != -1):
        scores.append(inscore)
print("合計%d人の学生" % (len(scores)))
for score in scores:
    total += score
average = total/(len(scores))
print("このクラスの総合の成績は：%d点、平均点は：%5.2f点" % (total,average))