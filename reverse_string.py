def find_first_repeated_number(sequence):
    for j in range(1, len(sequence)):
        for i in range(0, j):
            if sequence[j] == sequence[i]:
                print(sequence[j])
                return
    print("No repeated number found.")

find_first_repeated_number([1,2,3,1,3])