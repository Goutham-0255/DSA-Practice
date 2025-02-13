def rev_pyrammid(n):

    for i in range(0,n,1):

        # space
        for s in range(0,i,1):
            print(" ",end="")

        # PRINT  *
        for j in range(0,n-2*i+2,1):
            print("*",end="")

        # space
        for s in range(0,i,1): 
            print(" ",end="")

        print()

rev_pyrammid(5)