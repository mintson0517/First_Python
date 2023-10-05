scores = []
while True:
    inscore = input("学生の成績を入力してください：")
    if inscore == "":
        break

    scores.append(int(inscore))

scores2 = sorted(scores, reverse=True)
print("成績を小から大に並べ直します：", scores2)
