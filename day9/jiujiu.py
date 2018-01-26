i=1
while i<=9:
    j=1
    while j<=i:
        num=j*i
        print("%d*%d=%d" % (j, i, num), end="   ")
        j+=1
    print("")
    i+=1
