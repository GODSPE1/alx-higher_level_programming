#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10)

if l == 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,l))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, l))
elif 0 < last_digit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, l))
