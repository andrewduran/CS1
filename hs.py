def hs(n):
    length = 0
    while (n != 0):
        if (n % 2 == 0):
            print (n)
            n = n//2
            length = (length + 1)
        else:
            print (n)
            n = (3*(n+1))
            length = (length +1)
    if(n == 1):
            print (n)
            length = (length + 1)
            print (length)
            return None
    
