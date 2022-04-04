#Declaração de método que retorna a área de um quadrado com base no lado
def area_quadrado(lado):
    #Retorna a multiplicação de lado por lado
    return lado * lado

#Declaração de método que retorna o perímetro de um quadrado com base no lado
def perimetro_quadrado(lado):
    #Retorna a multiplicação do lado por 4
    return lado * 4

#Exibe na tela mensagem 'Lado do quadrado: ', e espera uma entrada do tipo float para guardar em valor_lado
valor_lado = float(input('Lado do quadrado: '))
#Chamada da função area_quadrado com o valor guardado na variável valor_lado
print('Area do quadrado:', area_quadrado(valor_lado))
#Chamada da função perimetro_quadrado com o valor guardado na variável valor_lado
print('Perímetro do quadrado: ', perimetro_quadrado(valor_lado))
