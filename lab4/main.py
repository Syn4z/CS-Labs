from data import expansionTable, sBoxes, permutationTable
import random


def generateRandomInput(length):
    return [random.randint(0, 1) for _ in range(length)]


def displayTable(table, tableName):
    print(f"{tableName} Table:")
    for i in range(0, len(table), 8):
        row = table[i:i + 8]
        formattedRow = " ".join(f"{item:2d}" for item in row)
        print(formattedRow)


def desRound(LiMinus1, RiMinus1, subkey):
    # Expand the 32-bit input to 48 bits
    expandedRiMinus1 = [RiMinus1[i - 1] for i in expansionTable]

    # XOR with the subkey
    xorResult = [int(expandedRiMinus1[i]) ^ int(subkey[i]) for i in range(48)]

    # Pass the result through S-boxes
    sBoxOutput = []
    for i in range(8):
        sBoxInput = xorResult[i * 6:(i + 1) * 6]
        row = int(str(sBoxInput[0]) + str(sBoxInput[5]), 2)
        col = int(''.join(map(str, sBoxInput[1:5])), 2)
        sBoxValue = sBoxes[i][row][col]
        sBoxOutput.extend([int(bit) for bit in format(sBoxValue, '04b')])

    # Permute the result using Permutation-table
    permutedResult = [sBoxOutput[i - 1] for i in permutationTable]

    # XOR with Li_minus_1 to get Ri
    Ri = [int(permutedResult[i]) ^ int(LiMinus1[i]) for i in range(32)]

    return Ri


LiMinus1Input = generateRandomInput(32)
print("LiMinus1: ", LiMinus1Input)
RiMinus1Input = generateRandomInput(32)
subkeyInput = generateRandomInput(48)
print("Subkey: ", subkeyInput)

displayTable(expansionTable, "Expansion")
displayTable(permutationTable, "\nPermutation")

resultRi = desRound(LiMinus1Input, RiMinus1Input, subkeyInput)
print(f"\nRi:\n{resultRi}")
