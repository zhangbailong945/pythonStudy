dict={'1':'zhangsan','2':'lisi','3':'wangwu','4':'zhaoliu'}
#访问字典
print(dict['2'])
print(dict['3'])
#修改字典
dict['2']='loach'
print(dict['2'])
#删除字典
del dict['2'] #删除键
print(dict)
#dict.clear() #清空字典
#print(dict)
#彻底删除字典
#del dict  #删除字典
str(dict)
print(type(dict))

#dict字典的函数
dict1={1:'zhangsan',2:'lisi',3:'wangwu',4:'zhaoliu'}
dict2={6:'hehe',7:'gg'}
seq=('one','two','three','four')
#创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
print(dict1.fromkeys(seq,10))
#根据键位获取值
print(dict1.get(1))
#判断键是否在字典里
print(1 in dict1)
#以列表返回可遍历的键值元组数组
print(dict1.items())
#以列表返回字典所有的键
print(dict1.keys())
#以列表返回字典所有的值
print(dict1.values())
#如果键不存在，将会添加键并设置为default为默认值
print(dict1.setdefault(5,'niubi'))
#把字典2的键值对更新到字典1里
print(dict1.update(dict2))
print(dict1)
#删除字典给定键key所对应的值，返回值为被删除的值。
print(dict1.pop(1))
#随机返回并删除字典中的一对键和值（一般删除末尾对）
print(dict1.popitem())

