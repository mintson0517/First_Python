dict1 = {"A": "犬", "B": "魚", "AB": "ちんあなご", "O": "お猿さん"}
name = input("あなたの血液型を入力してみてください：")
blood = dict1.get(name)

if blood is None:
    print("あなたが入力した" + name + "の血液データは記入されていません")
else:
    print(name + "型の性格などの特徴を血液型に例えると：" + blood)
