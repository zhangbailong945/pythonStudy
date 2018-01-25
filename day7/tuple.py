#创建一个元组
tuple1=('张三','李四','王五')
tuple2=(1,2,4,5,8)

#访问元组
print(tuple2)
print(tuple2[:2])
#修改元组，元组不能被修改，只能合并
print(tuple1+tuple2)
#删除元组,元组的值是不能删除的，但是可以删除整个元组
#del tuple1
#元组运算
print(len(tuple1)) #计算元组个数
print(tuple1+tuple2) #拼接元组
print(tuple1*2) #复制元组
print('张三' in tuple2) #判断元组的成员
for x in tuple1:
    print(x)

#元组的方法
len(tuple) #计算元组元素个数
max(tuple) #取元组中最大值
min(tuple) #取元组中最小值
tuple(seq) #将列表转换为元组