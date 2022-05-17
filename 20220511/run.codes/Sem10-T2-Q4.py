def showMenu():
    print(f'CÓDIGO  PRODUTO         PREÇO (R$)')
    print(f'H       Hamburger       5,50')
    print(f'C       Cheeseburger    6,80')
    print(f'M       Misto Quente    4,50')
    print(f'A       Americano       7,00')
    print(f'Q       Queijo Prato    4,00')
    print(f'X       PARA TOTAL DA CONTA')

def main():
    differenteFromX = True
    validOption = True
    sum = 0.0
    while(differenteFromX):
        showMenu()
        pickedOption = input().upper()[0]
        validOption = pickedOption in ['H','C','M','A','P','Q','X']
        differenteFromX = pickedOption != 'X'
        if (validOption):
            if (pickedOption == 'H'):
                sum += 5.5
            elif (pickedOption == 'C'):
                sum += 6.8
            elif (pickedOption == 'M'):
                sum += 4.5
            elif (pickedOption == 'A'):
                sum += 7.0
            elif (pickedOption == 'Q'):
                sum += 4.0
        else:
            print('Opção inválida.')
    print(f'{sum:.2f}')

if __name__ == "__main__":
    main()