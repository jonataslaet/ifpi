#Declaração de função que transforma minutos para horas com base nos minutos passados no parâmetro
def minutos_para_horas(qtd_minutos):
    #Coloca em horas a divisão inteira do que vem no parâmetro, por 60
    horas = qtd_minutos // 60
    #Coloca em minutos o resto da divisão inteira do que vem no parâmetro, por 60
    minutos = qtd_minutos % 60
    #Retorna a mensagem formatada HhMmin, onde H é o que tem em horas, e M é o que tem em minutos
    return f'{horas}h{minutos}min'

#Exibe na tela a mensagem "Quantidade de minutos: ", e espera uma entrada inteiro, para ser guardada em minutos
minutos = int(input('Quantidade de minutos: '))
#Coloca em horas a mensagem retornada pela função minutos_para_horas com base no que tem em minutos
horas = minutos_para_horas(minutos)
#Exibe na tela a mensagem com os minutos digitados e a mensagem contida em horas
print(f'{minutos} minutos são equivalentes a {horas}')
