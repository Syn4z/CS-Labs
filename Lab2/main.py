from playFairImpl import *


if __name__ == "__main__":

    match menu():
        case 1:
            result = checkInputs()
            print(result[0], result[1], result[2])

        case 2:
            encrypt()

        case 3:
            decrypt()
