def RTriangle(n):
    for i in range(0,n,1):
        for j in range(0,i,1):
            print('*' ,end=' ')
        print()
RTriangle(5)