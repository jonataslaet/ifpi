
num = int(input())
maior = num
menor = num
while(num != 0):
    if (num < menor):
        menor = num
    if (num > maior):
        maior = num
    num = int(input())

if menor != 0 and maior != 0:
    print(menor)
    print(maior)