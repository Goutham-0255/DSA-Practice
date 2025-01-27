def compare_num(n1,n2):
    compare =[
        (n1 > n1, ">"),
        (n1 >= n2, ">="),
        (n1 < n2, "<"),
        (n1 <= n2, "<="),
        (n1 == n2,"=="),
        (n1 != n2, "!="),
    ]

    for result,operator in compare:
        print(f"{n1} {operator} {n2} is {result}")


compare_num(20,30)