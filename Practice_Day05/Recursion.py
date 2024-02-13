def factorial(n):
    if n == 1:
        print(n)
        return 1 
    else: 
        print(n,"*",end = "")
        return n * factorial(n-1)
    
print(factorial(5))