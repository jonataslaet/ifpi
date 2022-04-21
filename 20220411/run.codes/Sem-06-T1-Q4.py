def isDigit(c):
    return '0' <= c <= '9'

if __name__ == "__main__":
    caractere = input().strip()
    print(isDigit(caractere))
