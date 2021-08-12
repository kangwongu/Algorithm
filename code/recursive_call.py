def factorial(data):
    if data > 1:
        return data * factorial(data - 1)
    else:
        return data



def factorial2(data):
    if data <= 1:
        return data
    
    return data * factorial(data - 1)
