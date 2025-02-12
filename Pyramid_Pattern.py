def pyramid(n):
    for i in range(0,n,1):

        # print space
        for s in range(0,n-i-1,1):
            print(" ",end="")
        # print *
        for j in range(0,2*i+1,1):
            print("*",end="")

        #print space
        for s in range(0,n-i-1,1):
            print(" ",end="")
        print()


        
pyramid(5)