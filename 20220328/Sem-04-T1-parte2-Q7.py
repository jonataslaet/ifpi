#Inverte os algarismos de um número de quatro dígitos
def inveter(numero):
    #Guarda em u o resto de divisão inteira de numero por 10
    u = numero % 10
    #Guarda em numero a divisão inteira de numero por 10
    numero = numero // 10
    #Guarda em d o resto da divisão de numero por 10
    d = numero % 10
    #Guarda em numero a divisão inteira de numero por 10
    numero = numero // 10
    #Guarda em c o resto da divisão de numero por 10
    c = numero % 10
    #Guarda em numero o resultado da divisão inteira de numero por 10
    numero = numero // 10
    #Guarda em m o resto da divisão de numero por 10
    m = numero % 10
    #Guarda em numero_invertido o resultado de u*1000 + d*100 + c * 10 + m 
    numero_invertido = (u * 1000) + (d * 100) + (c * 10) + m
    #Retorna o que tem em numero_invertido
    return numero_invertido

#Exibe na tela a mensagem "Digite um número entre 1000 e 9999: ", e espera uma entrada inteiro, para ser guardada em n
n = int(input("Digite um número entre 1000 e 9999: "))
#Exibe na tela uma mensagem com o número original e ele invertido, chamando a função inveter
print(f'O inverso de {n} é {inveter(n)}')
