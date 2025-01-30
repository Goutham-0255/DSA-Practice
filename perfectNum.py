def perfectnumber(num):


    divisors_sum = 0

    # check from 1 to number
    for i in range(1, num):

        # if the number is divisible by i it add that number to divisor and check with num
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num
print(perfectnumber(1))





