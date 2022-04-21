def eh_par(numero):
    return numero % 2 == 0

print('2 é par?', eh_par(2))
print('3 é par?', eh_par(3))
print('5 é ímpar?', not eh_par(5))
