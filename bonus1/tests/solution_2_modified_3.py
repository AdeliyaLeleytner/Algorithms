def factorial(n):
    if n == 0:
        result = 1
    result = n * factorial(n-1)
    return result