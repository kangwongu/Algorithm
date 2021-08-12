def func(n):
    if n < 1:
        return False
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return func(n-3) + func(n-2) + func(n-1)
