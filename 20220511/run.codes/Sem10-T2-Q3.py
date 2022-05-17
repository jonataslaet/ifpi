def showMenu():
    print(f'OPÇÕES:')
    print(f'1 - SAUDAÇÃO')
    print(f'2 - BRONCA')
    print(f'3 - FELICITAÇÃO')
    print(f'0 - FIM')
        




def main():
    
    differenteFromZero = True
    while(differenteFromZero):
        showMenu()
        pickedOption = int(input().strip())
        validOption = 0 <= pickedOption <= 3
        differenteFromZero = pickedOption != 0
        if (validOption):
            if (pickedOption == 1):
                print('1 - Olá. Como vai?')
            elif (pickedOption == 2):
                print('2 - Vamos estudar mais.')
            elif (pickedOption == 3):
                print('3 - Meus Parabéns!')
            elif (pickedOption == 0):
                print('0 - Fim de serviço.') 
        else:
            print('Opção inválida.')

if __name__ == "__main__":
    main()