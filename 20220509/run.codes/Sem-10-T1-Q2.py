
num = int(input().strip())
soma = 0
quantidade = 0
while(num != 0):
    quantidade += 1
    soma += num
    num = int(input().strip())

if soma > 0:
    print((soma/quantidade))
