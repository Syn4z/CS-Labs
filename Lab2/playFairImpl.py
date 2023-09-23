def encrypt():
    pass


def decrypt():
    pass


def menu():
    print("1. Input")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. Exit")
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice < 1 or choice > 3:
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
            if len(key) != 7:
                raise ValueError("Key must be 7 characters long")
            else:
                result.append(key)
                break
        except ValueError as e:
            print(e)
            continue

    while True:
        try:
            message = input("Enter message/cryptogram: ")
            if len(message) == 0:
                raise ValueError("Message is empty")
            for char in message:
                if char.isalpha():
                    message = message.replace(" ", "")
                    double_pairs = [message[i:i + 2] for i in range(0, len(message), 2)]
                    message = ' '.join(double_pairs).upper()
                    cryptogram = message.upper()
                    result.append(message)
                    result.append(cryptogram)
                    break
                else:
                    raise ValueError("Message must be a string from 'A' to 'Z' or 'a' to 'z'")
            break
        except ValueError as e:
            print(e)
            continue
    return result
