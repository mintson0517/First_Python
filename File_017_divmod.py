person = int(input("学生の人数を入力してください："))
apple = int(input("リンゴの総数を入力してください："))
ret = divmod(apple, person)
print("学生一人がもらえるリンゴの数は" + str(ret[0]) + "個")
print("リンゴの余りは" + str(ret[1]) + "個")
