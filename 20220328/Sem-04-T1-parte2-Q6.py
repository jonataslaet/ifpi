#Declaração de método que troca dois valores
def trocar(x1, x2):
    #Retorna os dois valores passados por parâmetro em posições invertidas
    return x2, x1
#Exibe na tela a mensagem "Primeiro número: ", e espera uma entrada inteiro, para ser guardada em n1
n1 = int(input('Primeiro número: '))
#Exibe na tela a mensagem "Segundo número: ", e espera uma entrada inteiro, para ser guardada em n2
n2 = int(input('Segundo número: '))
#Troca os valores de n1 e n2 chamando a função trocar
n1, n2 = trocar(n1, n2)
#Exibe uma mensagem com os valores do primeiro e segundo números
print(f'Primeiro {n1}; Segundo {n2}.')
