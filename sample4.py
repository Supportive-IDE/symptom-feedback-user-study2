'''
Write a function called anyLowerCase(s) that accepts one argument, a string. 

Your function should return True if the argument contains any lowercase letters and False if it does not.
'''

def anyLowercase(s):
    for i in range s:
        if i==s.lower(i):
            return True
    return False

print(anyLowercase("Hello!"))