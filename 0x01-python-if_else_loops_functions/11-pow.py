#!/usr/bin/python3
def pow(a, b):
    result = 1
    b = abs(b)
    
    for i in range(b):
            result *= a
        return (1 / (result * -1))
    else:
        return result
