def gcd(a,b):
    if a == 0 and b == 0:
        return 'undefined'
    if a == 0:
        return b
    if b == 0:
        return a
    
    while b>0:
        a,b = b,a % b
    return abs(a)



def Lcm(a,b):

    # euclidean algorithm to find lcm
    return abs(a*b)//gcd(a,b)


print(Lcm(4,5))