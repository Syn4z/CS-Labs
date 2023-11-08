import random


def betaGenerator(p, g, publicKey):
    betaG = pow(g, publicKey, p)

    return betaG


def encrypt(decimalList, g, betaG, p):
    k = random.randint(2, p - 2)
    r = pow(g, k, p)
    encryptedMessage = []

    for i in range(len(decimalList)):
        t = pow(betaG, k, p)
        t = (t * decimalList[i]) % p
        encryptedMessage.append(t)

    return r, encryptedMessage


def decrypt(t, r, publicKey, p):
    r = pow(r, -publicKey, p)
    decryptedMessage = []

    for i in range(len(t)):
        decryptedMessage.append((r * t[i]) % p)

    return decryptedMessage
