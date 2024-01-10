def tetration(x, n):

    if n == 0:
        return 1
    
    return x ** (tetration(x, n-1))
