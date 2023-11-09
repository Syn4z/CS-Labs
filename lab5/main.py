import math
import random
from lab5 import rsa
from lab5 import elGamal


# Function to convert ASCII to hexadecimal
def asciiToHex():
    inputHexString = ''
    inputString = input("Enter an ASCII string: ")
    for char in inputString:
        asciiCode = ord(char)
        hexCode = hex(asciiCode)[2:]
        inputHexString += hexCode
    return inputHexString


# Function to convert hexadecimal to decimal
def hexToDecimal(hex):
    try:
        decimalValue = int(hex, 16)
    except ValueError:
        print(f"Invalid hexadecimal input: {hex}")
        return None
    return decimalValue


# Function to convert decimal to ASCII
def decimalToAscii(decimal):
    try:
        asciiString = bytes.fromhex(hex(decimal)[2:]).decode("ASCII")
    except ValueError:
        print(f"Invalid decimal input: {decimal}")
        return None
    return asciiString


# Function to convert to 256 bits
def convertTo256Bits(key):
    res = key.to_bytes((key.bit_length() + 7) // 8, byteorder='big')
    if len(res) < 32:
        res = b'\x00' * (32 - len(res)) + res
    elif len(res) > 32:
        res = res[-32:]

    return res


if __name__ == "__main__":
    hexString = asciiToHex()
    decimalResult = hexToDecimal(hexString)
    p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2
    while True:
        choice = input("\nAlgorithm.\n1. RSA\n2. ElGamal\n3. Diffie-Hellman\n4. Exit\nEnter choice: ")
        if choice == '1':
            # --- RSA ---
            p1 = 54842563352743889723271906945023799461683912940473330029869582002758596244734047414942944302575401866079095165920866170992209481931096674209393130965016371435481884569442089655485749411699719574982471053192268121939770159938429226702886877620651221471881385973515832825501519676270464254882861356577526795533
            p2 = 238039718749478761511019596847354973295026075984876928633653257742855107710737471114249091228926171182269108653240517408263838748050742921792047806440477129321715740869371925409624933238787851825052787854111484624080866546330545373342919542105555763920510724168660349992256096389664239565705057893180586933583
            n = p1 * p2
            print("n length in decimal: ", len(str(n)))
            PhiN = (p1 - 1) * (p2 - 1)
            while True:
                e = random.randint(1, PhiN - 1)
                gcdEPhiN = math.gcd(e, PhiN)
                # Check if e is coprime with PhiN
                if gcdEPhiN == 1:
                    break
            d = pow(e, -1, PhiN)

            # print("E: ", e)
            # print("PhiN: ", PhiN)
            # print("D: ", d)
            print("\nDecimal message: ", decimalResult)
            encryptedMessage = rsa.encrypt(decimalResult, n, e)
            print("Encrypted message: ", encryptedMessage)
            decryptedMessage = rsa.decrypt(encryptedMessage, n, d)
            print("Decrypted decimal message: ", decryptedMessage)
            print("Decrypted ASCII message: ", decimalToAscii(decryptedMessage))

        elif choice == '2':
            # --- ElGamal ---
            k = random.randint(1, p - 2)
            publicKey = pow(g, k, p)
            betaGenerator = elGamal.betaGenerator(p, g, publicKey)

            print("\nDecimal message: ", decimalResult)
            r, t = elGamal.encrypt(decimalResult, g, betaGenerator, p)
            print("Encrypted message: ", r, t)
            decryptedText = elGamal.decrypt(t, r, publicKey, p)
            print("Decrypted decimal message:", decryptedText)
            print("Decrypted ASCII message: ", decimalToAscii(decryptedText))

        elif choice == '3':
            # --- Diffie-Hellman ---
            private1 = random.randint(2, p - 2)
            private2 = random.randint(2, p - 2)
            # Public keys
            public1 = pow(g, private1, p)
            public2 = pow(g, private2, p)
            # Shared secret
            shared1 = pow(public2, private1, p)
            shared2 = pow(public1, private2, p)
            convertTo256Bits(shared1)
            convertTo256Bits(shared2)

            print("\nShared 1 hex: ", convertTo256Bits(shared1).hex())
            print("Shared 1 decimal: ", int(convertTo256Bits(shared1).hex(), 16))
            print("Shared 2 hex: ", convertTo256Bits(shared2).hex())
            print("Shared 2 decimal: ", int(convertTo256Bits(shared2).hex(), 16))
        elif choice == '4':
            break
    