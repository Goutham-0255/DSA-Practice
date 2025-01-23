def first_repeated_number(num):
    for i in range(0, len(num)):

        #innner loop or pointer that commpare with i if the value is repeated
        for j in range(i+1, len(num)):

            #if repreated it return the value
            if num[i] == num[j]:  
                print(num[i])
                return
    print("No repeated number found.")

first_repeated_number([1, 2, 3, 1, 3])
