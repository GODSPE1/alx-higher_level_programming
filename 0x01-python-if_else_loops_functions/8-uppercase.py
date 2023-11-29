#!usr/bin/python3
def uppercase(str):
    for i in str:
    num = ord(i)
    if 97 <= num <= 122:
        print(chr(65 + num), end='')

