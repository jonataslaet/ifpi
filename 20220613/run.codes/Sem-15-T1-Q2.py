# 02.Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus
# Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as
# temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
# Fevereiro, ... ).

# Retorna temperatura de qualquer tipo (Celsius, Fahrenheit ou Kelvin) para graus Kelvin,
# com duas casas de arredondamento
def getTemperatureInKelvin(temperature, type):
    if (type.upper() == 'K'):
        return temperature
    if (type.upper() == 'C'):
        return temperature + 273.15
    return round(((temperature + 459.67) * (5/9)), 2)


# Retorna o nome do mês com base no id
def getNameOfMounthFromId(i):
    if (i == 0):
        return 'Janeiro'
    elif (i == 1):
        return 'Fevereiro'
    elif (i == 2):
        return 'Março'
    elif (i == 3):
        return 'Abril'
    elif (i == 4):
        return 'Maio'
    elif (i == 5):
        return 'Junho'
    elif (i == 6):
        return 'Julho'
    elif (i == 7):
        return 'Agosto'
    elif (i == 8):
        return 'Setembro'
    elif (i == 9):
        return 'Outubro'
    elif (i == 10):
        return 'Novembro'
    elif (i == 11):
        return 'Dezembro'


# Declaração da lista de temperaturas
listTemperature = []
sum = 0

# Percorre cada mês do ano (de 0 a 11)
for i in range(0, 12):
    # Recebe a temperatura
    t = float(input().strip())

    # Recebe o tipo de temperatura
    k = input().strip()

    # Captura a temperatura em formato kelvin e joga numa variável
    temperatureInKelvin = getTemperatureInKelvin(t, k)

    # Coloca dentro da lista a temperatura digitada pelo usuário, mas logo antes ela é convertida em kelvin
    listTemperature.append(temperatureInKelvin)

    # Soma a temperatura capturada
    sum += temperatureInKelvin

# Calcula a média das 12 temperaturas
average = sum/12

print("TEMPERATURA MÉDIA ANUAL")
print(f'{round(average, 2)}K')

print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
# Percorre as 12 temperaturas anteriormente listadas
for i in range(0, 12):
    # Verifica se a temperatura é maior que a média anteriormente calculada
    if (listTemperature[i] > average):
        # Se for, mostra o nome do mês e a temperatura daquele mês, que foi guardada em kelvin
        print(f'{getNameOfMounthFromId(i)}: {round(listTemperature[i], 2)}K')
