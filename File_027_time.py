import time as t

#print(t.time())  1970/01/01から現在までの秒数

week = ["月", "火", "水", "木", "金", "土", "日"]
time1 = t.localtime()
show = "現在時刻は：" + str(time1.tm_year) + "年"
show += str(time1.tm_mon) + "月" + str(time1.tm_mday) + "日"
show += str(time1.tm_hour)+"時"+str(time1.tm_min)+"分"
show += str(time1.tm_sec) +"秒 "+week[time1.tm_wday]+"曜日"
print(show)
