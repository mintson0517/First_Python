web = input("ウェブサイトのリンクを入力して下さい: ")

if web.startswith("https://") or web.startswith("http://"):
    print("リンクのフォーマットは正しいです")
else:
    print("リンクのフォーマットは間違っています")
