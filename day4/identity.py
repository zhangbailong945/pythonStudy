a=2
b=2
c=1
if(a is b):
    print('a and b is one object')
else:
    print('a,b is two object')

if( id(a)==id(b) ):
    print('a==b')
else:
    print('a!=b')

if(a is not c):
    print('a!=c')
else:
    print('a==c')

if( id(a) != id(c) ):
    print('a!=c')
else:
    print('a==c')