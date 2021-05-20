import time
import calendar
#timestamp:
timeX = time.time()
localtime = time.localtime(time.time())
lc1 = time.asctime(time.localtime(time.time()))
print ("your local time is: ", localtime)
print ("your time is: ", timeX)
print("your std lc is: ", lc1)


cal = calendar.month(2021, 3)
print(cal)