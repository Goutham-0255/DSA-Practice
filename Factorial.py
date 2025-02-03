def Factorial(num):

    # starts from 1 bacause when i use 0 its always ends in result 0 
    result = 1 


    # multiplies i to the result each time
    for i in range(1,num+1):
        result *= i

    return result

print(Factorial(10))