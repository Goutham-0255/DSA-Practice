def reversed_list(list):

    reversed_list = []

    #loop through each item in the list    
    for item in list:

        #the value will be inserted at index 0 everytime         
        reversed_list.insert(0, item)  
    return reversed_list


numbers = [1, 2, 3, 4, 5]
print(reversed_list(numbers))
