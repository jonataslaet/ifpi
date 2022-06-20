# 04.A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em
# mil unidades.
# Faça um programa que:
# a) leia os dados da tabela pelo teclado;
# b) leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
# c) determine e exiba o ano de maior volume geral de vendas.
# d) determine e exiba a média anual de vendas de cada fabricante durante o período.

# Declaracao da tupla de carros
cars = ['Fiat', 'Ford', 'GM', 'Wolkswagen']

sumsOfYear = []
bestYearOfSelling = 2013

# Declaracao de matriz (inicialmente só tem uma linha, mesma coisa de um vetor unidimensional)
matrix = []

# a) leia os dados da tabela pelo teclado;
# Percorre cada carro c
for c in range(0, 4):
    # A linha C está inicialmente vazia
    linha = []
    # Percorre cada quantidade vendida do c no ano y
    for y in range(2013, 2019):
        value = int(input().strip())
        if (c == 0):
            sumsOfYear.append(value)
        else:
            sumsOfYear[y-2013] += value
        # Adiciona o value à linha C
        linha.append(value)

    # Adiciona a linha C à matrix
    matrix.append(linha)

year = int(input().strip())

# Considera que inicialmente a quantidade mais vendida é a primeira
b = matrix[0][year-2013]

# Considera que inicialmente o fabricante que mais vendeu é o primeiro
mark = cars[0]

# Percorre cada carro
for c in range(0, 4):
    # Verifica se a quantidade vendida desse carro no ano year é maior que b
    if (matrix[c][year-2013] > b):
        # Se for, b é o novo maior, e mark é o cars[c]
        b = matrix[c][year-2013]
        mark = cars[c]

# b) leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
print(
    f'A fabricante que mais vendeu em {year} foi a {mark} com {b} mil unidades.')

# Considera que inicialmente o melhor ano de vendas é o de 2013
bestSumOfSelling = sumsOfYear[0]

# Percorre as somas de vendas em cada ano, de 2013 a 2018
for y in range(2013, 2019):
    if (sumsOfYear[y-2013] > bestSumOfSelling):
        bestYearOfSelling = y
        bestSumOfSelling = sumsOfYear[y-2013]

# c) determine e exiba o ano de maior volume geral de vendas.
print(
    f'O ano de maior volume geral de vendas foi {bestYearOfSelling} com {bestSumOfSelling} mil unidades.')

# d) determine e exiba a média anual de vendas de cada fabricante durante o período.
# Começa considerando sum = 0
sum = [0, 0, 0, 0]
for i in range(0, 4):
    for j in range(2013, 2019):
        sum[i] += matrix[i][j-2013]

print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
for i in range(4):
    print(f'A {cars[i]} vendeu em média {round(sum[i]/6, 2)} unidades por ano.')
