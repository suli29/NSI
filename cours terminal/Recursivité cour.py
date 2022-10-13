"""
def somme(n) :
    if n == 0 :
        return 0
    else :
        return n + somme(n-1)
    
print(somme(3))
"""

def fibonacci(n):
    if n == 0 : 
        return 0
    elif n == 1 :
        return 1
    else : 
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))