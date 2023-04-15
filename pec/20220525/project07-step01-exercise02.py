def getAlphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def getEncryptedLetter(key, letter):
    positioning = getAlphabet().find(letter)
    newPositioning = (positioning + key) % 26
    return getAlphabet()[newPositioning]


key = int(input("Por favor, entre com sua chave: "))

letter = input("Por favor, entre com uma letra para criptografar: ")

print("Sua letra criptografada é", getEncryptedLetter(key, letter))