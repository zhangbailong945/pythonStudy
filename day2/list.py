list=['abc',786,2.23,80,[1,2,3,4,5]]
list2=[5,6,7,8,9]

#输出List列表中的元素
print(list)
print(list[0]) #abc
print(list[1:3]) #786,2.23
print(list[3:]) #第三个开始所有的元素
print(list2*2)
print(list+list2)

#改变list列表中的元素
print(list)
list[0]=666
list[1:4]=[1,2,3]
print(list)
list[1:3]=[5,6]
print(list)
list[1:2]=[6]
print(list)
