import string
a='zhang bai long'
c="fsfadf\tsfsafaf"
d='sfdfsafa11233'
e='123123'
f='zhangbailong'
b="张佰龙"
b_utf8=b.encode('UTF-8')
b_gbk=b.encode('GBK')
#将字符串的第一个字符转换为大写
print(a.capitalize())
#返回一个指定宽度居中的字符串
print(a.center(40,'-'))
#返回一个字符在字符串中出现的次数
print(a.count('ng'))
print(a.count('ng',4,14))
#返回字符串的长度
print(len(a))
#编码后
print(b_utf8)
print(b_gbk)
#解码后
print(b_utf8.decode('UTF-8'))
print(b_gbk.decode('GBK'))
#判断字符串是不是以某个字符串开始
print(a.startswith('zhang'))
#判断字符串是不是以某个字符串结尾
print(a.endswith('long'))
#将字符串中的tab转换为空格
print(c.expandtabs())
#从原字符串中找到指定字符串，并返回索引值，没有返回-1
print(a.find('a'))
#从原字符串中找到指定字符串，并返回索引值，没有报错。
print(a.index('a'))
#如果字符串中至少有个字符，且所有的字符都是数字或者字符  则返回true
print(d.isalnum())
#如果字符串中至少有一个字符，且所有的字符都是字符，则返回true
print(f.isalpha())
#如果字符串中至少有一个字符,且所有的字符都是数字，则返回true
print(e.isdigit())
#如果字符串中至少有一个字符，且所有的字符都是小写。
print(f.islower())
#将字符串所有的单词格式化 首字母大写
print(a.title())
#判断字符串是否为title格式化
print(a.title().istitle())
#判断字符串中智商有一个字符，且所有字符都是数字
print(e.isnumeric())
g=" "
#判读字符串中是否有一个字符，且所有字符都是空格
print(g.isspace())
#
h="ZHANGBAILONG"
print(h.isupper())
#以字符串作为分割，将seq中的字符合并为一个新的字符
str1='-'
str2=''
seq=("l","o","a","c","h")
print(str1.join(seq))
print(str2.join(seq))
#返回一个原字符串左对齐，并使用空格填充指定长度的新字符串
print(str1.ljust(4,'*'))
str3=' loach '
print(str3.lstrip())
print(str3.rstrip())
print(str3.strip())
intab='abcde'
outtab='12345'
str4='zhang bai long'
#创建字符映射的转换表，第一个参数是字符串，另外一个是转换后的字符串
trantab=str4.maketrans(intab, outtab)
print(str4.translate(trantab))
print(max(str4))
print(min(str4))
print(str4.replace('zhang', 'wang'))
print(str4.rjust(20,'*'))

print(str4.split())
print(str4.split('a',1))
print(str4.split('g'))
print(str4.swapcase())
print(str4.zfill(20))