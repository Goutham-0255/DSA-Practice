def is_prime(n):

    # if less than 1 not prime 
    if n <= 1:
        return False
    
    # CHECK THE number 2 - square of the n 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

