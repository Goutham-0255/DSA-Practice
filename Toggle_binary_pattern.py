def binary_pattern(n):
    for i in range(n):
        if i % 2 == 0:
            start = "0"
        else:
            start = "1"

        for j in range(i + 1):
            print(start, end="")

            if start == "0":
                start = "1"
            else:
                start = "0"

        print()

binary_pattern(5)