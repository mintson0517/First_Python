import random as r

print("英語のアルファベットを一つ入力するとサイコロが回ります。\n終了したい場合はEnterキー")
while True:
    inkey = input("入力欄：")
    if len(inkey) > 0:
        num = r.randint(1, 6)
        print("サイコとの数は、" + str(num) + "\n")
    else:
        print("ゲームの幕が閉ざされました。")
        break
