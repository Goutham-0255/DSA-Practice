def RT_Number(n):
    for i in range(1,n+1,1):
        for j in range(1,n-i+2,1):
            print(j,end="")
        print()

RT_Number(5)