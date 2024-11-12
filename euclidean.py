#euclidean algorithm 
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)
print(gcd(35,15))


#advanced euclidean algorithm
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
a = 35
b = 15
gcd, x, y = gcd_extended(a, b)
print(f"gcd({a}, {b}) = {gcd}, x = {x}, y = {y}")
