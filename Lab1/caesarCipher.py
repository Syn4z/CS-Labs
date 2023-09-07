defaultAlphabet = (list(map(chr, range(ord('A'), ord('Z') + 1))))
defaultAlphabet = ' '.join(defaultAlphabet).replace(" ", "")


def keyAlphabet(key=""):
    if not key:
        return defaultAlphabet

    key += defaultAlphabet
    newAlphabet = key[0]

    for i in key:
        if i not in newAlphabet:
            newAlphabet += i

    return newAlphabet


def caesarCipherImpl(text, firstKey, sign, alphabet=None):
    if alphabet is None:
        alphabet = keyAlphabet()

    result = ""

    for char in range(len(text)):
        pos = (alphabet.index(text[char]) + sign * firstKey) % 26
        result += alphabet[pos]

    return result
