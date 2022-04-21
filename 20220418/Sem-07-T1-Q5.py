def getIMC(m, a):
    return m / (a * a)

if __name__ == "__main__":
    massa = float(input().strip())
    altura = float(input().strip())
    imc = getIMC(massa, altura)
    print(f'{imc:0.0f}')
    if (imc < 18.5): 
        print(f'Abaixo do peso')
    elif (imc < 25): 
        print(f'Peso normal')
    elif (imc < 30): 
        print(f'Sobrepeso')
    elif (imc < 35): 
        print(f'Obeso leve')
    elif (imc < 40): 
        print(f'Obeso moderado')
    elif (imc >= 40): 
        print(f'Obeso mórbido')