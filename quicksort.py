import random

def quicksort(arr):
    # If the array has 1 or no elements, it's already sorted, so just return it.
    if len(arr) <= 1:
        return arr

    # Pick a random element as the pivot.
    pivot = random.choice(arr)

    # Create an empty list for numbers smaller than the pivot.
    left = []
    for i in arr:
        if i < pivot:
            left.append(i)

    # Create an empty list for numbers larger than the pivot.
    right = []
    for i in arr:
        if i > pivot:
            right.append(i)

    # Create a list for numbers that are equal to the pivot.
    middle = []
    for i in arr:
        if i == pivot:
            middle.append(i)

    # Recursively sort the left and right parts and combine them with the pivot values.
    return quicksort(left) + middle + quicksort(right)

# Test the quicksort function
arr = [1]
print(quicksort(arr))
