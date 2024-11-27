def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % phi

# Example values for p, q, and e
p = 13
q = 17
e = 35

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    raise ValueError("Public key e is not coprime with φ(n)")

d = mod_inverse(e, phi)

print("Public Key (n, e):", (n, e))
print("Private Key (d):", d)