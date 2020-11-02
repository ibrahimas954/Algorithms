import math

def is_square(n):    
    val = math.sqrt(n)
    if val.is_integer():
        return True
    else:
        return False
    

print(is_square(21))