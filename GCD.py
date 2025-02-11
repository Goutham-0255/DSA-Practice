def gcd(a, b):


    # if both the value is 0 it is undefined cuz 0 cant be divided
    if a == 0 and b == 0:
        return 'undefined'
    
    #its euclidean algorithm to find gcd the loop ends when b hits 0 and the a is gcd
    while b:
        a, b = b, a % b
    return a

print(gcd(0,16))