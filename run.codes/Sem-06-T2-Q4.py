def isDigit(c):
    return '0' <= c <= '9'

def isLetter(c):
    return "A" <= c.upper() <= "Z"

def showCaractere(c):
    return isLetter(c) or isDigit(c)

if __name__ == "__main__":
    letra = input().strip()
    print(showCaractere(letra))
