
# Leitura do lado do quadrado
side = int(input().strip())

# Vetor que pega as duas dimensões do menor valor, e o próprio menor valor
bigger = [-1, -1, -1]

# Vetor que pega as duas dimensões do maior valor, e o próprio maior valor
shorter = [-1, -1, -1]

# Captura os valores de cada célular do quadrado
for i in range(0, side):
    for j in range(0, side):
        value = int(input().strip())
        if (value > bigger[2]):
            bigger[0] = i
            bigger[1] = j
            bigger[2] = value
        if (shorter[2] == -1 or value < shorter[2]):
            shorter[0] = i
            shorter[1] = j
            shorter[2] = value

# Exibe o resultado
print(f'({bigger[0]}, {bigger[1]})')
print(f'({shorter[0]}, {shorter[1]})')
