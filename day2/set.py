number={1,22,3,5,6,2,4,7,5}
print(number)
if(1 in number):
    print("1在number集合里")
else:
    print("1不在number集合里")

#集合运算
a=set('1234')
b=set('3456')
print(a-b)   #a和b的差集 1,2,5,6
print(a|b)  #a和b的并集1256
print(a&b)  #a和b的交集34
print(a^b) #a和b中不同时存在的元素1256
