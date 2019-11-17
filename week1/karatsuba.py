from math import ceil, floor
from sys import argv


def main():
    while len(argv) != 3:
        print("Usage: python karatsuba.py number1 number2")
        exit(1)

    x = int(argv[1])
    y = int(argv[2])

    p = karatsuba(x, y)
    print("\n{x} * {y} = {p}".format(x=x, y=y, p=p))


def karatsuba(x, y):
    lengthX = len(str(x))
    lengthY = len(str(x))

    if lengthX == 1 or lengthY == 1:
        return x * y

    halfN = max(lengthX, lengthY) / 2
    multiplier = 10 ** halfN

    a = x / multiplier
    b = x % multiplier
    c = y / multiplier
    d = y % multiplier

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    adbc = karatsuba(a + b, c + d) - ac - bd

    product = ac * 10**(2*halfN) + adbc * multiplier + bd
    return product


if __name__ == "__main__":
    main()
