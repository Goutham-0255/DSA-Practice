import random

def quicksort(arr):
    
    #check if arr less tha1 1 
    if len(arr) <= 1:
        return arr

    #choose random value
    pivot = random.choice(arr)

    #store the i value in left if it is less than pivot
    left = []
    for i in arr:
        if i < pivot:
            left.append(i)

    #store in right if it is higher than pivot 
    right = []
    for i in arr:
        if i > pivot:
            right.append(i)

    #store in middle if it is equal to pivot
    middle = []
    for i in arr:
        if i == pivot:
            middle.append(i)


    #using quicksort function do the same thing again and again until the array sorted 
    return quicksort(left) + middle + quicksort(right)

arr = [1]
print(quicksort(arr))
