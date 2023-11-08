def encrypt(decimalList, n, e):
    encryptedMessage = []
    for decimal in decimalList:
        encryptedMessage.append(pow(decimal, e, n))
    return encryptedMessage


def decrypt(encryptedMessage, n, d):
    decryptedMessage = []
    for part in encryptedMessage:
        decryptedMessage.append(pow(part, d, n))
    return decryptedMessage
