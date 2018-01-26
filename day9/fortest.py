a='abcdefg'
b=(1,2,3,4,5)
c=['one','two','three','four']
#遍历字符串
for x in a:
    print(x)

#遍历元组
for x in b:
    print(x)

#遍历列表
for x in c:
    print(x)

#遍历 数字序列
for x in range(10):
    print(str(x),end=',')

#continue
for x in 'zhangbailong':
    if(x=='a'):
        continue
    print(x,end=',')