#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    sum = 0
    for j in range(1, n):
        sum = sum + int(sys.argv[j])
        print(sum)
