def get_size(measurement): 
    if 35 <= measurement < 38:
        size = 'S'
    elif 38 <= measurement < 41:
        size = 'M'
    elif 41 <= measurement < 44:
        size = 'L'
    else:
        size = 'not available'
    return size
    print(size)