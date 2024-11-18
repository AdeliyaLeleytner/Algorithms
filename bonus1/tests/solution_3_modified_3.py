def fibonacci(n):
    if n <= 1:
        result = n
    result = fibonacci(n-1) + fibonacci(n-2)
    return result