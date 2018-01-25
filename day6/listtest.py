#创建列表
list=[1,2,3,4,5,6]
number=[7,8,9,0]
#访问列表
print(list)
print(list[0])
#更新列表
list[0]=9
print(list)
#删除列表成员
del list[0]
print(list)
#获取列表长度
print(len(list))
#组合
print(list+number)
#重复列表
print(list*2)
#判断成员是否存在
print(1 in list)
#迭代
for x in list:
    print(x,end=" ")

#list常用方法
print(len(list))  #获取list长度
print(max(list)) #获取最大值
print(min(list)) #获取最小值

print(list)
#在列表后面添加一个新的值
list.append(5)
print(list)
#统计某个元素在列表中出现的次数
print(list.count(5))
#在列表末尾添加多个值
list.extend([6,6,6])
print(list)
#在列表中找出某个值在列表中第一次出现的索引位置
print(list.index(6))
#在列表中插入一个元素
list.insert(0,9)
print(list)
#从列表中删除一个元素，默认是从末尾开始i
list.pop()
print(list)
list.pop(list[1])
print(list)
#移除列表中的某个值
list.remove(9)
print(list)
#反转列表
list.reverse()
print(list)
#对列表进行排序
list.sort()
print(list)
#复制列表
j=list.copy()
print(j)
#清空列表
list.clear()
print(list)
