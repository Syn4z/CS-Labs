from playFairImpl import *


if __name__ == "__main__":
    inputData = []
    key = ""
    message = ""
    encryptedMessage = []
    matrix = []
    while True:
        choice = menu()
        match choice:
            case 1:
                encryptedMessage = []
                inputData = checkInputs()
                key = prepareKey(inputData[0])
                matrix = createMatrix(key)
                print("Matrix:")
                for row in matrix:
                    print(' '.join(row))

            case 2:
                if len(inputData) == 0:
                    print("You must enter input first")
                    continue
                encryptedText = ""
                message = insertBetweenRepeating(inputData[1])
                message = prepareText(message)
                encryptedMessage = [crypt(pair, matrix, "encrypt") for pair in message]
                for i in range(len(message)):
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
