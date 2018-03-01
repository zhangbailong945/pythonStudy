import re

print(re.match('www','www.loach.com').span())
print(re.match('com','www.loach.com'))


line="Cats are smarter than dogs"
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else:
    print("Not Match!")

print(re.search('www','www.laoch.com').span())
print(re.search('com','www.laoch.com').span())

phone="2004-956-2332 # 这是测试哈哈哈！"
num=re.sub(r'#.*$',"",phone)
print("电话号码：",num)

num=re.sub(r'\D',"",phone)
print("只剩下数字：",num)

def double(matched):
    value=int(matched.group('value'))
    return str(value*2)

s='A23G4HFD567'
print(re.sub('(?P<value>\d+)',double,s))

