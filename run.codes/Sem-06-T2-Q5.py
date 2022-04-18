def isDigit(c):
    return '0' <= c <= '9'

def isVowel(c):
    cm = c.upper()
    return cm == "A" or cm == "E" or cm == "I" or cm == "O" or cm == "U" 

def isLetter(c):
    return "A" <= c.upper() <= "Z"

def isConsonant(c):
    return (not (isVowel(c))) and isLetter(c)

def showCaractere(c):
    if isVowel(c): print("vogal")
    elif isConsonant(c): print("consoante")
    elif isDigit(c): print("número")
    elif (not isLetter(c)) and (not isDigit(c)) : print("símbolo")

if __name__ == "__main__":
    letra = input()
    print(showCaractere(letra))
