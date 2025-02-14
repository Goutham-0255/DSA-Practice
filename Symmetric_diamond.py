def diamond(n):
    for i in range(0,n,1):

        for s in range(0,n-i-1,1):
            print(" ",end="")

        for j in range(0,2*i+1,1):
            print("*",end="")

        print()

    for i in range(n-2,-1,-1):

        for s in range(0,n-i-1,1):
            print(" ",end="")

        for j in range(0,2*i+1,1):
            print("*",end="")

        print()



diamond(4)




            