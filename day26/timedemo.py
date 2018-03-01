import time


ticks=time.time()
print("当前时间戳：",ticks)

localtime=time.localtime(time.time())
print("本地时间为：",localtime)


#格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

print(time.strftime("%a %b %d %H:%S %Y",time.localtime()))

