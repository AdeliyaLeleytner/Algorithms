def fxctorixl(n):
    if n == 0:
        return 1
    return n * fxctorixl(n-1)