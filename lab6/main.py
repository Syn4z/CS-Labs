from lab5 import rsa, main
from data import *
import elGamalSignature
import rsaSignature


def decimalToHex(decimal):
    try:
        hexString = hex(decimal)[2:]
    except ValueError:
        print(f"Invalid decimal input: {decimal}")
        return None
    return hexString


if __name__ == "__main__":
    print("RSA:\n")
    n, e, d = rsaSignature.signMessage(p1, p2)
    hashDecimal = main.hexToDecimal(messageHash)
    encryptedMessage = rsa.encrypt(hashDecimal, n, e)
    decryptedMessage = rsa.decrypt(encryptedMessage, n, d)
    hexStringResult = decimalToHex(decryptedMessage)
    print(f"Decrypted Hash: {hexStringResult}\nOriginal Hash: {messageHash}")
    print(hexStringResult == messageHash)

    print("\nElGamal:\n")
    elGamalSignature.signMessage(g, p, hashDecimal)
