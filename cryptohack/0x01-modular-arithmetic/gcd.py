# This algorithm is my implementation of Euclid's Algorithm to calculate gcd(66528, 52920)


def gcd(a: int, b: int) -> int:
    print(f"gcd({a}, {b})")
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(66528, 52920))
