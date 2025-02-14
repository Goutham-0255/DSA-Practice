def rev_pyrammid(n):

    for i in range(0,n,1):

        # space
        for s in range(0,i,1):
            print(" ",end="")

        # PRINT  *
        for j in range(0,2*(n-i)-1,1):
            print("*",end="")

        # space can ignore this line did this to understand how space work during practice
        for s in range(0,i,1): 
            print(" ",end="")

        print()

rev_pyrammid(5)