def getAlphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def getEncryptedLetter(key, letter):
    positioning = getAlphabet().find(letter)
    newPositioning = (positioning + key) % 26
    return getAlphabet()[newPositioning]

def getCleanMessage(message):
    clearedMessage = ""
    for char in message:
        if char in getAlphabet():
            clearedMessage += char
    return clearedMessage

def getScrambledMessage(key, alphabet):
    encryptedMessage = ""
    for char in alphabet:
        if char in getAlphabet():
            encryptedMessage += getEncryptedLetter(key, char)
            key += 1
        else:
            encryptedMessage += char
    return encryptedMessage

if __name__ == "__main__":
    key = int(input("Por favor, entre com sua chave: "))
    message = input("Por favor, digite a mensagem a ser criptografada: ")
    scrambledMessage = getScrambledMessage(key, message)
    print("Sua mensagem criptografada é: ", getCleanMessage(scrambledMessage))