import sys

def fbo(n,w=0):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        print('%d,%d'%(a,b))
        counter+=1

f=fbo(10,0)

while True:
    try:
        print(next(f),end=" ")
    except:
        sys.exit()

