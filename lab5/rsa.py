def encrypt(decimal_list, n, e):
    encrypted_message = []
    for decimal in decimal_list:
        encrypted_message.append(pow(decimal, e) % n)
    return encrypted_message


def decrypt(encrypted_message, n, d):
    decrypted_message = []
    for part in encrypted_message:
        decrypted_message.append(pow(part, d) % n)
    return decrypted_message
