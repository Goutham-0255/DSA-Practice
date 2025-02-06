def perfectN(num):
    sum = 0



    for i in range(1,num-1):

        # check the number which are divisible and add them to the sum  
        if num % i == 0:
            sum += i
    return sum == num
        
print(perfectN(6))