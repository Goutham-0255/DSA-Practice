def numberPatternRT(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i, end="")
        print()
        
numberPatternRT(5)