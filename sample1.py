'''
Write a function called anyLowerCase(s) that accepts one argument, a string. 

Your function should return True if the argument contains any lowercase letters and False if it does not.
'''

def anyLowercase(s):
    list(s)
    for i in range(0, len (s)):
        if s[i] == 'a' or 'b' or 'c' or 'd':
            return True
        else:
            return False

print(anyLowercase("Hello!"))