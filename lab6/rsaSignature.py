import math
import random


def signMessage(p1, p2):
    n = p1 * p2
    # noinspection DuplicatedCode
    PhiN = (p1 - 1) * (p2 - 1)
    while True:
        e = random.randint(1, PhiN - 1)
        gcdEPhiN = math.gcd(e, PhiN)
        # Check if e is coprime with PhiN
        if gcdEPhiN == 1:
            break
    d = pow(e, -1, PhiN)

    return n, e, d
