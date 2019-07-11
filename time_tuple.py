import time

localtime = time.localtime(time.time())
print(localtime)

formattedTime = time.asctime(time.localtime(time.time()))
print(formattedTime)
