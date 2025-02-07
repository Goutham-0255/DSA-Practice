def pattern(n):

    for i in range(0,n,1):
        for j in range(0,n,1):
            print("*", end="")
        print()

pattern(5)