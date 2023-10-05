# 入力データ
score = [100, 90, 80]
jp = "国語"
math = "数学"
en = "英語"
# 出力
print(
    "%s成績：%d点\n" % (jp, score[0]),
    "%s成績：%d点\n" % (math, score[1]),
    "%s成績：%d点" % (en, score[2]),
)
