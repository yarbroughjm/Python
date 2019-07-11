import time
import datetime

print("Now it is", time.asctime(time.localtime(time.time())))
print("Tomorrow it will be", time.asctime(time.localtime(time.time() + 86400)))
print("A year ago it was", time.asctime(time.localtime(time.time() - (86400 * 365))))
print("In 100 hours it will be", time.asctime(time.localtime(time.time() + (86400 / 3600 * 100))))

birthday = datetime.datetime(1979, 4, 3, 14, 22)

print("I was born on", birthday.isoformat(' '))
