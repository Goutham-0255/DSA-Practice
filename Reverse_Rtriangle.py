def revRT(n):
    for i in range(0,n,1):
        for j in range(0,n-i,1):
            print("*",end="")
        print()

revRT(5)