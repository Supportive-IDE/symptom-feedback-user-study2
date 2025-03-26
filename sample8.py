'''
Write a function called createNumberBlock(n) that has one parameter, n, a positive 
integer. The function should print a block of numbers. A block is n lines long and 
each line, i, should be made up of the numbers between i and i + n (exclusive).

For example, createNumberBlock(5) should print:
12345
23456
34567
45678
56789
'''

def createNumberBlock(n):
    for i in range(1,n+1):
        num = ''
        for j in range(i,i+n):
            num += str(j)
        print(str(num))

createNumberBlock(5)