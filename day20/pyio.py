import sys
#读取键盘输入 raw_input和Input，区别input可以接受表达式
'''
str=input("请输入：")
print("你输入的内容是："+str)
'''
#文件I/O open(filename,mode)
'''
file=open('foo.txt','wb')
print("文件名：",file.name)
print("访问模式：",file.mode)
print("文件是否关闭：", file.closed)
file.close()
'''

#文件write(str)
'''
file=open('foo.txt','wb')
file.write(b"zhangbailongcom\n")
file.close()
'''
#write 写入字符串
'''
file=open('foo.txt','w')
file.write("loachblog.com\n")
file.close()
'''

#write 追加字符串
'''
file=open('foo.txt','a')
file.write("zhangbailong.com\n")
file.close()
'''
#read 读取文件内容
'''
file=open('foo.txt','r')
str=file.read()
file.close()
print(str)
'''

#read 读取单独一行
'''
file=open('foo.txt','r')
str=file.readline()
file.close()
print(str)
'''
'''
f=open('foo.txt','r')
str=f.readlines()
print(str)
f.close()
'''

#迭代
'''
f=open('foo.txt','r')
for line in f:
    print(line,end='')
f.close()
'''

#f.tell() 返回文件对象当前所处位置
#f.seek() 如果要改变文件当前的位置，可以使用f.seek(offset,from_what)函数



