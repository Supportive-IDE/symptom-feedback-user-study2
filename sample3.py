'''
Write a function called get_size(measurement) that accepts one argument, a number. The function should 
return a string representing the size associated with the measurement. Sizes are determined as follows:

- Measurements between 35 (inclusive) and 38 (exclusive) are size 'S'.
- Measurements between 38 (inclusive) and 41 (exclusive) are size 'M'.
- Measurements between 41 (inclusive) and 44 (exclusive) are size 'L'.

If the provided measurement is outside the ranges above, the function should return 'not available'.
'''

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


print(get_size(40))