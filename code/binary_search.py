def binary_search(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False
    
    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)
