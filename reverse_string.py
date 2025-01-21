def find_first_repeated_number(sequence):
    # Iterate through the sequence, starting from the second element
    for j in range(1, len(sequence)):
        # Check all previous elements for a match with the current element
        for i in range(0, j):
            if sequence[j] == sequence[i]:  # Found a repeated number
                print(sequence[j])
                return
    # If no repeated number is found after checking all elements
    print("No repeated number found.")

find_first_repeated_number([1, 2, 3, 1, 3])
