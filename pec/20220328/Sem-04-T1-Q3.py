def elevadoA3(n):
    resultado = n ** 3
    return resultado

if __name__ == "__main__":
    numero = int(input())
    print(f'O valor desse número elevado ao cubo é {numero}', elevadoA3(numero))
