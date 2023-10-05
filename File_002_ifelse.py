# ログインシステム
pw = input("パスワードを入力してください")
if pw == "1234":
    print("ログインが完了しました。")
else:
    print("パスワードが間違っています。")

# テストの成績
score = input("成績を入力してください")
if int(score) >= 90:
    print("A")
elif int(score) >= 80:
    print("B")
elif int(score) >= 70:
    print("C")
else:
    print("D")

# discount
money = int((input("金額を入力してください。")))
if money >= 1000:
    if money >= 10000:
        print(money * 0.8, end="円\n")
    elif money >= 8000:
        print(money * 0.9, end="円\n")
    elif money >= 5000:
        print(money * 0.9, end="円\n")
    else:
        print(money, end="円\n")
