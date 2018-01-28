#列表推导式
vec=[2,4,6]
vec2=[3*x for x in vec]
print(vec2) #6,12,18

#使用if过滤
vec3=[3*x for x in vec if x>3]
print(vec3) #12,18

#嵌套列表
#将3x4列表转换为4x3列表
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
vec4=[[row[i] for row in matrix] for i in range(4)]
print(vec4)

#遍历字典
dict={'name':'zhangsan','age':12,'sex':'男'}
for k,v in dict.items():
    print(k,v)