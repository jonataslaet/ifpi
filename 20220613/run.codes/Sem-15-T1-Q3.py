# 03.Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e
# devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente:
# a) a soma dos elementos da primeira linha
# b) a soma dos elementos da última coluna
# c) a média de todos os elementos
# d) o menor elemento
# e) o maior elemento

# Declaração da soma dos elementos da primeira linha
a = 0

# Declaração da soma dos elementos da última coluna
b = 0

# Declaração da soma e média de todos os elementos
sum = 0
c = 0

# Declaração do menor elemento
d = -1

# Declaração do maior elemento
e = -1

# Declaracao de matriz (inicialmente só tem uma linha, mesma coisa de um vetor unidimensional)
matrix = []

# Captura valores 'n' e 'm'
n = int(input().strip())
m = int(input().strip())

# Percorre a matriz
for i in range(n):
    row = []
    for j in range(m):
        value = int(input().strip())
        row.append(value)
        # Soma com sum o elemento guardado em value
        sum += value
        # Se for a primeira linha, some value com a
        if (i == 0):
            a += value
            # Se TAMBÉM a primeira coluna, menor e maior são iguais a value
            if (j == 0):
                d = value
                e = value

        # Se o valor digitado for menor que o menor, o novo menor é o value
        if (value < d):
            d = value
        # Se o valor digitado for maior que o maior, o novo maior é o value
        if (value > e):
            e = value

        # Se for a última coluna, some value com b
        if (j == m - 1):
            b += value
    matrix.append(row)

c = sum / (n*m)

print(f'({a}, {b}, {round(c,4)}, {d}, {e})')
