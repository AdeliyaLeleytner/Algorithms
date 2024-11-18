def fiyonxcci(n):
    if n <= 1:
        return n
    return fiyonxcci(n-1) + fiyonxcci(n-2)