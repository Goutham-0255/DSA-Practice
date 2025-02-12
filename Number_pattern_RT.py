def Rtriangle(n):
    for i in range(0,n+1,1):
        for j in range(1,i+1,1):
            print(j, end=" ")
        print()

Rtriangle(5)