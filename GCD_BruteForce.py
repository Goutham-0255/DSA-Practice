def GCD(a,b):

    # if the two numbers are 0 we need to print undefined cause 0 cant be divided
    if a == 0 and b == 0:
        return 'unidentified'
    
    # if either one of the number is 0 other one is the gcd
    if a == 0:
        return b
    if b == 0:
        return a


    # we can initiate hcf to 0 or 1 init isnt necessary here because we are chnaging the hcf to i in the loop
    hcf = 0
    for i in range(1,min(a,b)+1):


        # if both the i completly divisible by 0 it assign the i value to hcf and the hcf is returned
        if a % i == 0 and b % i == 0:
            hcf = i 
    return hcf
    
print(GCD(9,16))