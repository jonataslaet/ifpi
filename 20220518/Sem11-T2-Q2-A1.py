#0, 1, 1, 2, 3, 5, 8, 13, ...
# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = 3
# f(5) = 5
# f(6) = 8
# f(7) = 13
# (...)


if __name__ == "__main__":
    n = int(input().strip())

    # Reserva uma memorização com (n+1) espaços, todos eles com valor NULL
    memorization = [0] * (n+1)

    # Preenche a memorização com os dois primeiros números
    memorization[0] = 0
    memorization[1] = 1

    # Preenche a memorização com o terceiro termo até o enésimo termo
    for i in range(2, n+1):
        memorization[i] = memorization[i-1] + memorization[i-2]

    # Concatena em result o primeiro valor da memorização
    result = str(memorization[0])

    # Concatena em result uma vírgula, um espaço e um valor da mamorização
    for i in range(1, n):  # isso do segundo valor em diante
        result = result + ', ' + str(memorization[i])

    # Exibe o valor de result
    print(result)
