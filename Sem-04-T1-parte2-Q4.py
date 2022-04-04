#Declaração de método que calcula o valor percentual com base no valor e na porcentagem
def percentual(valor, porcentagem):
    #Retorna o valor multiplicado pela divisão da porcentagem por 100
    return valor * (porcentagem / 100)

#Exibe na tela a mensagem "Preço: ", e espera uma entrada float, para ser guardada em pr
pr = float(input("Preço: "))
#Exibe na tela a mensagem "Percentual: ", e espera uma entrada float, para ser guardada em vr_p
vr_p = float(input("Percentual: "))
#Coloca em pr_acres o valor de pr somado ao valor calculado pela função percentual
pr_acres = pr + percentual(pr, vr_p)
#Coloca em pr_desc o valor de pr subtraído do valor calculado pela função percentual
pr_desc = pr - percentual(pr, vr_p)
#Exibe a mensagem com o valor original, com o percentual de acréscimo e com a soma dos dois
print(f'R${pr} com acréscimo de {vr_p}% fica por R${pr_acres}')
#Exibe a mensagem com o valor original, com o percentual de desconto e com a subtração dos dois
print(f'R${pr} com desconto de {vr_p}% fica por R${pr_desc}')
