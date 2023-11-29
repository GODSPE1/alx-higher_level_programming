#!/usr/bin/python3
def pow(a, b):
    result = 1
    a = abs(a)
    b = abs(b)

    for i in range(b):
            result *= a
    if a < 0:
        return (result * -1)
    elif b < 0:
        return (1 / (result * -1))
    else:
        return result
