import time, datetime
date_now = time.localtime()
date_now2 = ("{}/{}/{}".format(date_now[2],date_now[1],date_now[0])).split("/")
_date = datetime.date(int(date_now2[2]), int(date_now2[1]), int(date_now2[0]))

print(date_now)
print(date_now2)
print(_date)
print(datetime.datetime(date_now[0], date_now[1], date_now[2], date_now[3], date_now[4], date_now[5], date_now[6]))