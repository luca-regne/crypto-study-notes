# This algorithm is my implementation of Euclid's Algorithm to calculate gcd(66528, 52920)

def euclids_algorithm(a: int, b: int) -> int:
    print(f"gcd({a}, {b})")
    if b == 0:
        return a
    else:
        return euclids_algorithm(b, a % b)


print(euclids_algorithm(66528, 52920))
