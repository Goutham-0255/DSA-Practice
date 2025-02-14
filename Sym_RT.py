'''def RT(n):

    for i in range(0,n,1):

        for j in range(0,i+1,1):
            print("*",end="")

        print()

    for i in range(n-2,-1,-1):

        for j in range(0,i+1,1):
            print("*",end="")

        print()
RT(4)'''



'''string method'''

def RT(n):
    for i in range(0,n,1):

        print("*" * (i+1))

    for i in range(n-2,-1,-1):
        
        print("*"*(i+1))


RT(3)