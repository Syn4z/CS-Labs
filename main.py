from caesarAlgorithm import *


print("\nCaesar Cipher")

alphabet = basic_alphabet
key_1 = ""
key_2 = ""
msg = ""

while 1:

    print("\nMenu")
    print("1. Enter first key")
    print("2. Enter second key")
    print("3. Enter your encrypted/non-encrypted message")
    print("4. Print input data")
    print("5. Reset input data")
    print("6. Encrypt message")
    print("7. Decrypt  message")
    print("8. Exit")

    num = input("\nEnter your choice: ")

    match num:
        case "1":
            key_1 = valid_key_input()

        case "2":
            key_2 = valid_text_input(1)
            alphabet = key_alphabet(key_2)

        case "3":
            msg = valid_text_input()

        case "4":
            print("\nMessage:", msg)
            print("Key 1:", key_1)
            print("Key 2:", key_2)
            print("Alphabet:", alphabet)

        case "5":
            alphabet = basic_alphabet
            key_1 = ""
            key_2 = ""
            msg = ""

        case "6":
            if not (msg and key_1):
                print("Missing key or text message")
            else:
                sign = 1
                new_msg = caesar_cipher(msg, key_1, sign, alphabet)
                print("\nEncrypted message:", new_msg)

        case "7":
            if not (msg and key_1):
                print("Missing key or text message")
            else:
                sign = -1
                new_msg = caesar_cipher(msg, key_1, sign, alphabet)
                print("\nDecrypted message:", new_msg)

        case "8":
            exit(1)

        case _:
            print("Invalid input")
