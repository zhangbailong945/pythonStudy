class Person:
    name='baba'
    sex='nan'
    def say(slef):
        return 'hello human!'
    def __init__(self):
        print(self.__class__)

man=Person()
print(man.say())

class People:
    name=''
    age=0
    #定义私有属性，私有属性在类的外部无法直接访问
    __weight=0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))

#单继承示例
class Student(People):
    grade=''
    def __init__(self,n,a,w,g):
        #调用父类的方法
        People.__init__(self,n,a,w)
        self.grade=g
    #覆盖父类的方法
    def speak(self):
        print("%s说：我%d岁了，我在读%d年纪"%(self.name,self.age,self.grade))

s=Student('ken',10,60,3)
s.speak()

#多继承
class Speaker():
    topic=''
    name=''
    def __init__(self,nt,):
        self.name=name
        self.topic=t
    def speak(self):
        print("我叫%s，我是一个演说家，我演讲的主题是%s"%(self.name,self.topic))

#多重继承实现
class Sample(Speaker,Student):
    a=''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)

test=Sample("loach",25,80,4,"python")
test.speak()

#类的私有属性和方法
class Boy:
    __secretCount=0 #私有变量
    publicCount=0 #公有变量
  
    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)

counter=Boy()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)
