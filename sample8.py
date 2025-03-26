def createNumberBlock(n):
    for i in range(1,n+1):
        num = ''
        for j in range(i,i+n):
            num += str(j)
        print(str(num))