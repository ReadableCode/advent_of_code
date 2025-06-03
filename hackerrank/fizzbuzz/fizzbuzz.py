#!/bin/python3

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#


def fizzBuzz(n):
    # Write your code here
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        print(i)


if __name__ == "__main__":
    n = int(input().strip())

    fizzBuzz(n)
