def getAlphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def getEncryptedLetter(key, letter):
    positioning = getAlphabet().find(letter)
    newPositioning = (positioning + key) % 26
    return getAlphabet()[newPositioning]


key = 12

word = "omqemd"

solution = ""
for i in range(0,len(word)):
    solution += getEncryptedLetter(key, word[i])
print(solution)