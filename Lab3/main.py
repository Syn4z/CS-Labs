from playFairImpl import *


def menu():
    print("1. Input")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. Exit")
    while True:
        try:
            result = int(input("Enter choice: "))
            if result < 1 or result > 4:
                raise ValueError("Choice must be 1-4")
            else:
                return result
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


if __name__ == "__main__":
    inputData = []
    inputKey = ""
    inputMessage = ""
    encryptedMessage = []
    matrix = []
    while True:
        choice = menu()
        match choice:
            case 1:
                encryptedMessage = []
                inputData = checkInputs()
                inputKey = prepareKey(inputData[0])
                matrix = createMatrix(inputKey)
                print("Matrix:")
                for row in matrix:
                    print(' '.join(row))

            case 2:
                if len(inputData) == 0:
                    print("You must enter input first")
                    continue
                encryptedText = ""
                inputMessage = insertBetweenRepeating(inputData[1])
                inputMessage = prepareText(inputMessage)
                encryptedMessage = [crypt(pair, matrix, "encrypt") for pair in inputMessage]
                for i in range(len(inputMessage)):
                    encryptedText += encryptedMessage[i]
                print(f'Encrypted text: {encryptedText}')

            case 3:
                if len(inputData) == 0:
                    print("You must enter input first")
                    continue
                elif not encryptedMessage:
                    if len(inputData[1]) % 2 != 0:
                        print("You must enter valid cryptogram")
                        continue
                    else:
                        encryptedMessage = prepareText(inputData[1])
                decrypt = [crypt(pair, matrix, "decrypt") for pair in encryptedMessage]
                if "".join(decrypt).endswith("Z"):
                    print(f'Decrypted text: {"".join(decrypt)[:-1]}')
                else:
                    print(f'Decrypted text: {"".join(decrypt)}')

            case 4:
                exit()
