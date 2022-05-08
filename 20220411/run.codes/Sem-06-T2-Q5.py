def isDigit(c):
    return '0' <= c <= '9'

def isVowel(c):
    cm = c.upper()
    return cm == "A" or cm == "E" or cm == "I" or cm == "O" or cm == "U" 

def isLetter(c):
    return "A" <= c.upper() <= "Z"

def isConsonant(c):
    return (not (isVowel(c))) and isLetter(c)

if __name__ == "__main__":
    letra = input()
    if isVowel(letra): print("vogal")
    elif isConsonant(letra): print("consoante")
    elif isDigit(letra): print("número")
    elif (not isLetter(letra)) and (not isDigit(letra)) : print("símbolo")
