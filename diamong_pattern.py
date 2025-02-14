def diamond(n):

    for i in range(0,n,1):

        # print space
        for s in range(0,n-i-1,1):
            print(" ",end="")
        # print *
        for j in range(0,2*i+1,1):
            print("*",end="")

        #print space not need but did it understand when practice to understand
        '''for s in range(0,n-i-1,1):
            print(" ",end="")'''
        print()


    for i in range(0,n,1):

        # space
        for s in range(0,i,1):
            print(" ",end="")

        # PRINT  *
        for j in range(0,2*(n-i)-1,1):
            print("*",end="")

        # space can ignore this line did this to understand how space work during practice
        '''for s in range(0,i,1): 
            print(" ",end="")'''
        
        print()



diamond(5)