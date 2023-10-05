# print sep=間に入れる文字
print(100, "Hello World in Python on Mintson's desktop PC", 100, sep="&")

# score
name = "Mintson"
score = 100
print("%sの成績は、%d点です" % (name, score))

# space
price = 23.8
print("価格は、%8.2f円です" % price)

# format
score = 60
print("{}の成績は、{}".format(name, score))

# total score
japanese = int(input("国語の成績を入力して下さい："))
mathematics = int(input("数学の成績を入力してください："))
english = int(input("英語の成績を入力してください："))

total = japanese + mathematics + english
average = total / 3

print("国語の成績：{}\n数学の成績：{}\n英語の成績：{}\n".format(japanese, mathematics, english))
print("君の総合点は、{}点です".format(total))
print("君の総合点は、{:.2f}点です".format(average))
