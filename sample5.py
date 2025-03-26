'''
Write a function called get_name() that prompts the user to enter their name. The function 
should return the name. Test the function by calling it and printing a message that greets 
the user by their name. For example, if the user's name is Frodo, your code should print 
something along the lines of 'Hello, Frodo'.
'''

def get_name():
    name= input('What is your name? ')
    return name
    
get_name()
print('Hello', name)