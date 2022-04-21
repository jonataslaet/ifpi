def isVowel(c):
    cm = c.upper()
    return cm == "A" or cm == "E" or cm == "I" or cm == "O" or cm == "U" 

def showLetter(c):
    return "A" <= c.upper() <= "Z" and (not isVowel(c))

if __name__ == "__main__":
    letra = input().strip()
    print(showLetter(letra))
