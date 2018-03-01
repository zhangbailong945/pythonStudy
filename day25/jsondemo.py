import json

#将字典转换为json

data={
    'name':'zhangsan',
    'sex':'男',
    'url':'zhangbailong.com'
}

json_str=json.dumps(data)
print("python原始数据：",repr(data))
print("json对象：",json_str)

#将json对象转换为python字典
data2=json.loads(json_str)
print("data2['name']",data2['name'])
print("data2['url']",data2['url'])