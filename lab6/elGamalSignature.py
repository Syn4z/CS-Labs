import random


def signMessage(g, p, hashDecimal):
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    k = 79
    r = pow(g, k, p)
    s = (hashDecimal - (x * r)) * pow(k, -1, p - 1) % (p - 1)
    if 1 < r < p - 1 and 0 < s < p - 1:
        v1 = (pow(y, r, p) * pow(r, s, p)) % p
        v2 = pow(g, hashDecimal, p)
        if v1 == v2:
            print("Signature is valid")
