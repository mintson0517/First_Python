listname = ["Mintson", "Monkey", "Kindle"]
listmath = [100, 50, 80]
listen = [100, 60, 80]
listph = [100, 70, 60]

print("名前     番号  数学  英語  物理")
for i in range(0, 3):
    print(
        listname[i].ljust(8),
        str(i + 1).rjust(3),
        str(listmath[i]).rjust(5),
        str(listen[i]).rjust(5),
        str(listph[i]).rjust(5)
    )
