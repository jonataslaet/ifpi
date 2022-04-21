def somaDeTresNumeros(a, b, c):
    soma = a + b + c;
    return soma

def mediaDe3(f, g, h):
    media = somaDeTresNumeros(f, g, h)/3
    return media

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    print(mediaDe3(x, y, z))
