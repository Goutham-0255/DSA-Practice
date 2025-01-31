def fibonacci(n):
    fibonacci_series = [0, 1]

    # loop through 2 to num and add the value store it in fib
    for i in range(2, n):
        fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    return fibonacci_series

n = 10
result = fibonacci(n)
print(result)
