from rsa import *
import gmpy2

# Function to convert ASCII to hexadecimal
def ascii_to_hex():
    hex_string = ''
    input_string = input("Enter an ASCII string: ")
    for char in input_string:
        ascii_code = ord(char)
        hex_code = hex(ascii_code)[2:]
        hex_string += hex_code
    return hex_string


# Function to convert hexadecimal to ASCII
def decimal_to_ascii(decimal_list):
    ascii_string = ''
    for decimal_value in decimal_list:
        try:
            ascii_character = chr(decimal_value)
            ascii_string += ascii_character
        except ValueError:
            print(f"Invalid decimal input: {decimal_value}")
            return None
    return ascii_string


def hex_to_decimal(hex_list):
    decimal_list = []
    for hex_value in hex_list:
        try:
            decimal_value = int(hex_value, 16)
            decimal_list.append(decimal_value)
        except ValueError:
            print(f"Invalid hexadecimal input: {hex_value}")
            return None
    return decimal_list


n = 3599
e = 7
m = 3480
d = pow(e, -1, m)
hex_string = ascii_to_hex()
hex_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
decimal_result = hex_to_decimal(hex_list)
print(decimal_result)
encrypted_message = encrypt(decimal_result, n, e)
print(encrypted_message)
decrypted_message = decrypt(encrypted_message, n, d)
print(decrypted_message)
print(decimal_to_ascii(decrypted_message))
