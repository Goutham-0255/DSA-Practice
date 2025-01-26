def merge_sort(arr):
    
    # only start when the array has more than 1 value
    if len(arr) > 1:

        # find the middle and split it left and right
        mid = len(arr)//2
        left_array = arr[:mid]
        right_array = arr[mid:]

        # do the same for the splited arrays until they are single value
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        # sort the splited arrays and merge it
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        # merge the remaining values
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1 
            k += 1
            

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

    return arr
print(merge_sort([12,3,2,5,3,6])) 