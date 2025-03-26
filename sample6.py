'''
Write a function called hasTwoDigits(x) that has one parameter, a positive integer. The 
function should return True if the integer is two digits long and False otherwise. You 
can assume that the argument is always a valid positive integer.
'''

def hasTwoDigits(x):
    a = str(x)
    if len(a) == 2:
        return True
    else:
        return False

print(hasTwoDigits(10))
print(hasTwoDigits(5))