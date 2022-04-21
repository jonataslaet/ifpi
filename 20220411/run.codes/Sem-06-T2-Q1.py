def showVowel(c):
    cm = c.upper()
    return cm == "A" or cm == "E" or cm == "I" or cm == "O" or cm == "U" 

if __name__ == "__main__":
    letra = input().strip()
    print(showVowel(letra))
