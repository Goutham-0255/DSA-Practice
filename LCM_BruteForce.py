def Lcm(a,b):
    max_num = max(a,b)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

print(Lcm(4,2))