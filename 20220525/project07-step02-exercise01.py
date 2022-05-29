def getAlphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def getEncryptedLetter(key, letter):
    positioning = getAlphabet().find(letter)
    newPositioning = (positioning + key) % 26
    return getAlphabet()[newPositioning]

message = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

encryptedMessage = ""

key = int(input("Por favor, entre com a chave: "))

for char in message:
    if char in getAlphabet():
        encryptedMessage += getEncryptedLetter(key, char)
    else:
        encryptedMessage += char
print("Sua mensagem criptografada é: ", encryptedMessage)