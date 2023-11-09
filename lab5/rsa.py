def encrypt(decimal, n, e):
    encryptedMessage = pow(decimal, e, n)
    return encryptedMessage


def decrypt(encryptedMessage, n, d):
    decryptedMessage = pow(encryptedMessage, d, n)
    return decryptedMessage
