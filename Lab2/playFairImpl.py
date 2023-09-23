import random


def crypt(pair, matrix, operation):
    encryptedPair = ""
    decryptedPair = ""
    letter1, letter2 = pair
    row1, col1 = None, None
    row2, col2 = None, None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == letter1:
                row1, col1 = row, col
            elif matrix[row][col] == letter2:
                row2, col2 = row, col

    if operation == "encrypt":
        if row1 != row2 and col1 != col2:
            encryptedPair = matrix[row1][col2] + matrix[row2][col1]
        elif row1 == row2:
            encryptedPair = matrix[row1][(col1 + 1) % len(matrix[row1])] + matrix[row2][(col2 + 1) % len(matrix[row2])]
        elif col1 == col2:
            encryptedPair = matrix[(row1 + 1) % len(matrix)][col1] + matrix[(row2 + 1) % len(matrix)][col2]
        return encryptedPair
    elif operation == "decrypt":
        if row1 != row2 and col1 != col2:
            decryptedPair = matrix[row1][col2] + matrix[row2][col1]
        elif row1 == row2:
            decryptedPair = matrix[row1][(col1 - 1) % len(matrix[row1])] + matrix[row2][(col2 - 1) % len(matrix[row2])]
        elif col1 == col2:
            decryptedPair = matrix[(row1 - 1) % len(matrix)][col1] + matrix[(row2 - 1) % len(matrix)][col2]
        return decryptedPair


def menu():
    print("1. Input")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. Exit")
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice < 1 or choice > 4:
                raise ValueError("Choice must be 1-4")
            else:
                return choice
        except ValueError as e:
            print(e)
            continue


def checkInputs():
    result = []
    while True:
        try:
            key = input("Enter key: ")
            for char in key:
                if not char.isalpha() and char != " ":
                    raise ValueError("Key must be a string from Romanian alphabet")
            if len(key) <= 7:
                raise ValueError("Key must be at least 7 characters long")
            result.append(key)
            break
        except ValueError as e:
            print(e)
            continue

    while True:
        try:
            message = input("Enter message/cryptogram: ")
            if len(message) == 0:
                raise ValueError("Empty input not allowed")
            for char in message:
                if not char.isalpha() and char != " ":
                    raise ValueError("Message must be a string from Romanian alphabet")
            result.append(message)
            break
        except ValueError as e:
            print(e)
            continue
    return result


def insertBetweenRepeating(message):
    for i in range(len(message) - 1):
        if message[i] == message[i + 1]:
            message = message[:i + 1] + random.choice(["Q", "X", "Z"]) + message[i + 1:]
    return message


def prepareText(message):
    message = message.replace(" ", "")
    message = message.upper()
    message = message.replace("J", "I")
    result = []
    message = insertBetweenRepeating(message)
    if len(message) % 2 != 0:
        message += "Z"
    group = 0
    for i in range(2, len(message), 2):
        result.append(message[group:i])
        group = i
    result.append(message[group:])
    return result


def prepareKey(key):
    key = key.replace(" ", "")
    key = key.upper()
    key = key.replace("J", "I")
    result = ""
    for char in key:
        if char not in result:
            result += char
    return result


def createMatrix(key):
    alphabet = [char for char in 'AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ']
    for char in key:
        if char in alphabet:
            alphabet.remove(char)
    matrix = [[None] * 5 for _ in range(6)]
    key_index = 0

    for row in range(6):
        for col in range(5):
            if key_index < len(key):
                matrix[row][col] = key[key_index]
                key_index += 1

    for row in range(6):
        for col in range(5):
            if matrix[row][col] is None and alphabet:
                matrix[row][col] = alphabet.pop(0)
    return matrix
