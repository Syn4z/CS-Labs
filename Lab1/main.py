from caesarCipher import *


if __name__ == "__main__":

    print("Welcome to Caesar Cipher Implementation")

    alphabet = defaultAlphabet
    textMessage = ""
    encryptedMessage = ""
    firstKey = ""
    secondKey = ""

    while True:
        print("\nCommands:")
        print("1. Enter text message")
        print("2. Enter encrypted message")
        print("3. Enter first key")
        print("4. Enter second key")
        print("5. Encrypt message")
        print("6. Decrypt message")
        print("7. Show data entered")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                textMessage = input("Enter the text message: ").replace(" ", "").upper()
                if not textMessage.isalpha():
                    print("Invalid input text message. It should contain only letters from the Latin alphabet.")
                    continue
            case '2':
                encryptedMessage = input("Enter the encrypted message: ").replace(" ", "").upper()
            case '3':
                firstKey = input("Enter the first key (integer between 1 and 25): ")
                if not firstKey.isdigit() or not (1 <= int(firstKey) <= 25):
                    print("Invalid key. It should be an integer between 1 and 25.")
                    continue
            case '4':
                secondKey = input("Enter the second key (only latin alphabet letters, at least length 7): ").replace(" ", "").upper()
                alphabet = keyAlphabet(secondKey)
                print("New alphabet:", alphabet)
                if not secondKey.isalpha() or len(secondKey) < 7:
                    print("Invalid key. It should contain only latin alphabet letters and have a length of at least 7.")
                    continue
            case '5':
                sign = 1
                if not textMessage:
                    print("Please enter a text message.")
                    continue
                if not firstKey:
                    print("Please enter a first key.")
                    continue
                encryptedMessage = caesarCipherImpl(textMessage, int(firstKey), sign, alphabet)
                print("Encrypted Message:", encryptedMessage)
            case '6':
                sign = -1
                decryptedMessage = caesarCipherImpl(encryptedMessage, int(firstKey), sign, alphabet)
                print("Decrypted Message:", decryptedMessage)
            case '7':
                print("Text Message:", textMessage)
                print("Encrypted Message:", encryptedMessage)
                print("First Key:", firstKey)
                print("Second Key:", secondKey)
            case '8':
                exit()
            case _:
                print("Invalid choice. Please enter a valid option from (1-8).")
                continue
