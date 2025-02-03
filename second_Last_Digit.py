def secondLastDigit(num):



    # floor division will reduce the last number by rounding it off when divided by 10
    num = num // 10


    # that remaining numbers modulus of 10 is the second last digit number
    result = num % 10

    return result

print(secondLastDigit(122452))