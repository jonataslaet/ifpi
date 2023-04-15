alphabet = "abcdefghijklmnopqrstuvwxyz"

key = 3

letter = input("Por favor, entre com uma letra para criptografar: ")

positioning = alphabet.find(letter)

newPositioning = (positioning + key) % 26

encryptedLetter = alphabet[newPositioning]

print("Sua letra criptografada é", encryptedLetter)