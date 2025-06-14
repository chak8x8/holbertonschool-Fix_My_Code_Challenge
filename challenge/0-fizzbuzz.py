#!/usr/bin/python3
import sys

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        elif i % 3 == 0:
            output = "Fizz"
        elif i % 5 == 0:
            output = "Buzz"
        else:
            output = str(i)
        print(output, end=" " if i < n else "")
    print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fizzbuzz(int(sys.argv[1]))
