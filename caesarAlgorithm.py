# Create a list of characters from A to Z
basic_alphabet = (list(map(chr, range(ord('A'), ord('Z') + 1))))
# Transform the list into a string and remove spaces
basic_alphabet = ' '.join(basic_alphabet).replace(" ", "")


def valid_text_input(key_2=0):
    while 1:
        text = input("Enter text/word: ").replace(" ", "").upper()
        length = len(text)

        if key_2 and length < 7:
            print("Your text should contain 7 or more characters")
        else:
            for i in range(length):
                if text[i] not in basic_alphabet:
                    print("Your text should contain only letters (a-z, A-Z)")
                    break

                if i == length - 1:
                    return text


def valid_key_input():
    while 1:
        key = input("Enter key: ")
        try:
            key = int(key)
        except:
            print("Input an integer key between 1 and 25")
            continue
        if key < 1 or key > 25:
            print("Input an integer key between 1 and 25")
        else:
            return key


def key_alphabet(key=""):
    if not key:
        return basic_alphabet

    # Combine the key with the basic_alphabet
    key += basic_alphabet
    new_alphabet = key[0]

    # Check for each unique element in key and if it's missing from new_alphabet add it
    for i in key:
        if i not in new_alphabet:
            new_alphabet += i

    return new_alphabet


def caesar_cipher(msg, key_1, sign_value, alphabet=key_alphabet()):
    new_msg = ""

    for i in range(len(msg)):
        # Check for the index in the alphabet of the character msg[i]
        # Sign value of -1 represents decryption and 1 encryption
        pos = (alphabet.index(msg[i]) + sign_value * key_1) % 26
        new_msg += alphabet[pos]

    return new_msg
