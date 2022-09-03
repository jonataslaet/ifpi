def sair():
    exit


def escolher_menu(opcao):
    if opcao == 7:
        sair()


def menu_principal():
    try:
        print('1 - Nova consulta (agendamento)')
        print('2 - Pagar Consulta')
        print('3 - Cancelar consulta')
        print('4 - Agendar retorno')
        print('5 - Relatório de consultas realizadas no mês por médico')
        print('6 - Relatório de faturamento da clínica por mês')
        print('7 - Sair')
        opcao_escolhida = int(input('Opção escolhida: '))
        if (opcao_escolhida < 1 or opcao_escolhida > 7):
            print('Opção inválida. Tente novamente.')
            menu_principal()
        escolher_menu(opcao_escolhida)
    except:
        print('Opção inválida. Tente novamente.')
        menu_principal()


if __name__ == "__main__":
    menu_principal()
