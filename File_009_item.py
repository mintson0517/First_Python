subjects=["国語","数学","英語"]
item = [12,"Hello","World"]
for item in item:
    print(item)
    
#score
scores = [100,90,80]
for i in range(len(scores)):
    print("%sの成績：%d点" % (subjects[i],scores[i]))