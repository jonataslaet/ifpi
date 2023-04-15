
num = int(input())
soma = 0
quantidade = 0
while(num != 0):
    quantidade += 1
    soma += num
    num = int(input())

print(f'{(soma/quantidade)}')