# lcm


from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(48, 18))  # Output: 144