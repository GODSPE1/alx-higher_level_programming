#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if num >= 97 and num <= 122:
            num -= 32
        num = chr(num)
        print("{}".format(num), end='')
    print("")
