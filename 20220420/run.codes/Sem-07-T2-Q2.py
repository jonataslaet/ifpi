def isPar(num):
    return num % 2 == 0


if __name__ == "__main__":
    num = int(input().strip())
    qtdPares = 0
    d1 = num//100
    d2 = (num//10) % 10
    d3 = num % 10
    if (isPar(d1) and d1 > 0):
        qtdPares = qtdPares + 1
    if (isPar(d2)):
        qtdPares = qtdPares + 1
    if (isPar(d3)):
        qtdPares = qtdPares + 1
    print(qtdPares)
