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
def hexToDecimal(hexList):
    decimalList = []
    for hexValue in hexList:
        try:
            decimalValue = int(hexValue, 16)
            decimalList.append(decimalValue)
        except ValueError:
            print(f"Invalid hexadecimal input: {hexValue}")
            return None
    return decimalList


# Function to convert decimal to ASCII
def decimalToAscii(decimalList):
    asciiString = ''
    for decimalValue in decimalList:
        try:
            asciiCharacter = chr(decimalValue)
            asciiString += asciiCharacter
        except ValueError:
            print(f"Invalid decimal input: {decimalValue}")
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
    inputHexList = [hexString[i:i + 2] for i in range(0, len(hexString), 2)]
    decimalResult = hexToDecimal(inputHexList)
    p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2
    while True:
        choice = input("\nAlgorithm.\n1. RSA\n2. ElGamal\n3. Diffie-Hellman\n4. Exit\nEnter choice: ")
        if choice == '1':
            # --- RSA ---
            p1 = 8482479315149711950752258241110685314001838485416728105804731601342472973795852911739243577339861314095318358245834095429585187184004022565567908771263422669893711243824244855913109999706238841329300762170462045030705210983947528164446487077594465965760641249900028865948594406689800467024028321852130716558248436365007780677418936582531255846411199179081722995287278237255413488951987812862529422118126498077704071476019640808578595518618126458081444043091122745452569671740280181972295799024823039889406723463082859723019760526766771798336590014715239210526524660949379567978930407371131889123290087275336549957933485264432885096781398196966413566504960395669788279528464772788102323629637613569193282009166499603708109626055778464818740851368052156686159705573740598111576732628464351651867067052980153258580238181116657054032583863740554962751346308017435763969431958849752041879156414427392273351587484069959077182551264915462361118287733993881698757376545760812000397126011013357583441783160833
            p2 = 8422174289009636854445291649470660777659668403913992328921836065831491846921188702564875940350756264668230177511065648525154616347875117852123393310327198064616899198980841511755204059608493685446306187095282538735675238980280074855759603868904866827900899888722400465298226241947035284457074860783147182497102213931313125452515186768678742002093951204279599113759748048607553190361646952598645156070697675598555366082074258397747678261111689921471274950665577023317299550038299669409491699409913543160500035215803341585524384827968097123624470860171052817712314003096615865105687368625640556679061584159024219319902495428185971528554393853409096755489118142062697060478723758672077394086362319689636167464554364452993500466711561010901560270515791008393276706608082481622203853119534110458758951465097825743355117746309141870015108225925427737936747415795862706806133924956855604733744169460203128464652888433703128517057404765556638690128677346216831136502744875808496537095013809057506838884384769
            n = p1 * p2
            PhiN = (p1 - 1) * (p2 - 1)
            while True:
                e = random.randint(1, PhiN - 1)
                gcdEPhiN = math.gcd(e, PhiN)
                # Check if e is coprime with PhiN
                if gcdEPhiN != 1:
                    continue
                else:
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
    