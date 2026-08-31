# This algorithm is my implementation of Euclid's Algorithm to calculate gcd(66528, 52920)

def egcd(a: int, b: int):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


print(egcd(26513, 32321))
