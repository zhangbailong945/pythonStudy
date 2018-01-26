list=['2',1,'zhangsan','666']
it=iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for x in iter(list):
    print(x,end='\n')
