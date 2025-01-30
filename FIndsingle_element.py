def singleNumber(nums):
    result = 0
    for num in nums:


        # cancel out repeating number and save the single occuring numebr
        result ^= num  
    return result

print(singleNumber([2,3,4,2,3,8,4]))
