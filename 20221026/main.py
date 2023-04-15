from Clinica import Clinica
from Consulta import Consulta
from Database import Database
from Medico import Medico


def sair():
    exit


def buscar_elemento_por_indice(lista, indice):
    for i in range(len(lista)+1):
        if indice == i:
            return lista[i]
    return None


def selecionar_clinica(database):
    print('Selecione a clínica: ')
    # Variável para indicar o índice da clínica neste menu
    c = 1

    # Captura do database as clínicas disponíveis nele
    clinicasDisponiveis = database.getClinicas()
    try:
        # Percorre cada clínica da lista de clínicas disponíveis, mostrando-as em um menu
        for clinica in clinicasDisponiveis:
            print('%d - %s' % (c, clinica.getNome()))
            c += 1

        # Captura do usuário a opção escolhida para a clínica
        opcao_escolhida = int(input('Opção escolhida: '))

        # Se a opção escolhida for menor que 1 ou maior que a quantidade de clínicas disponíveis,
        # Então exiba que a opção escolhida foi inválida e executa novamente este método
        if (opcao_escolhida < 1 or opcao_escolhida > len(clinicasDisponiveis)):
            print('Opção inválida. Tente novamente.')
            selecionar_clinica(database)

        # Se chegou bem aqui nesta linha, então passou nas validações anteriores
        return buscar_elemento_por_indice(clinicasDisponiveis, opcao_escolhida-1)
    except:
        print('Opção inválida. Tente novamente.')
        selecionar_clinica(database)


def selecionar_medico_por_clinica(clinica):
    print('Clínica Escolhida: ' + clinica.getNome())
    print('Selecione o médico: ')
    # Variável para indicar o índice do médico neste menu
    m = 1

    # Captura do database as clínicas disponíveis nele
    medicosQueAtendemNestaClinica = clinica.getMedicos()
    try:
        # Percorre cada clínica da lista de clínicas disponíveis, mostrando-as em um menu
        for medico in medicosQueAtendemNestaClinica:
            print('%d - %s' % (m, medico.getNome()))
            m += 1

        # Captura do usuário a opção escolhida para o médico
        opcao_escolhida = int(input('Opção escolhida: '))

        # Se a opção escolhida for menor que 1 ou maior que a quantidade de médicos desta clínica,
        # Então exiba que a opção escolhida foi inválida e executa novamente este método
        if (opcao_escolhida < 1 or opcao_escolhida > len(medicosQueAtendemNestaClinica)):
            print('Opção inválida. Tente novamente.')
            selecionar_medico_por_clinica(clinica)

        # Se chegou bem aqui nesta linha, então passou nas validações anteriores
        return buscar_elemento_por_indice(medicosQueAtendemNestaClinica, opcao_escolhida-1)
    except:
        print('Opção inválida. Tente novamente.')
        selecionar_medico_por_clinica(clinica)


def criar_consulta(database):
    clinicaEscolhida = selecionar_clinica(database)
    medicoEscolhido = selecionar_medico_por_clinica(clinicaEscolhida)
    dia, mes, ano = selecionar_dia_mes_ano()
    consulta = Consulta(clinicaEscolhida, medicoEscolhido, dia, mes, ano)
    mostrar_consulta(consulta)
    database.addConsulta(consulta)
    mostrar_consulta(consulta)

def mostrar_consulta(consulta):
    print('Dados da consulta:')
    print('Número de autorização: %d' % (consulta.getAutorizacao()))
    print('Médico: %s' % (consulta.getMedico().getNome()))
    print('Clínica: %s' % (consulta.getClinica().getNome()))
    print('Data: %d/%d/%d' % (consulta.getDia(), consulta.getMes(), consulta.getAno()))
    print()
def selecionar_dia():
    try:
        dia = int(input('Selecione o dia: '))
        if (dia < 1 or dia > 31):
            print('Dia inválido. Tente novamente.')
            selecionar_dia()
        return dia
    except:
        print('Dia inválido. Tente novamente.')
        selecionar_dia()

def selecionar_mes():
    try:
        mes = int(input('Selecione o mês: '))
        if (mes < 1 or mes > 12):
            print('Mês inválido. Tente novamente.')
            selecionar_mes()
        return mes
    except:
        print('Mês inválido. Tente novamente.')
        selecionar_mes()

def selecionar_ano():
    try:
        ano = int(input('Selecione o ano: '))
        if (ano < 1 or ano > 9999999):
            print('Ano inválido. Tente novamente.')
            selecionar_ano()
        return ano
    except:
        print('Ano inválido. Tente novamente.')
        selecionar_ano()

def confirmar_pagamento_consulta(consulta):
    try:
        opcao = int(input('Tem certeza de que deseja pagar esta consulta? (1 - Sim, 2 - Não)'))
        if opcao < 1 or opcao > 2:
            print('Opção inválida. Tente novamente.')
            confirmar_pagamento_consulta(consulta)
        consulta.pagar()
        print('Consulta paga com sucesso.')
    except:
        print('Opção inválida. Tente novamente.')
        confirmar_pagamento_consulta(consulta)
def pagar_consulta(database):
    try:
        autorizacao = int(input('Digite o número de autorização da consulta: '))
        if autorizacao < 1:
            print('Número de autorização inválido. Tente novamente.')
            pagar_consulta(database)
        consulta_encontrada = buscar_elemento_por_indice(database.getConsultas(), autorizacao)
        if consulta_encontrada is not None:
            confirmar_pagamento_consulta(consulta_encontrada)
            mostrar_consulta(consulta_encontrada)
        else:
            print('Consulta não encontrada')
            menu_principal(database)
    except:
        print('Número de autorização inválido. Tente novamente.')
        pagar_consulta(database)
def selecionar_dia_mes_ano():
    dia = selecionar_dia()
    mes = selecionar_mes()
    ano = selecionar_ano()
    return dia, mes, ano

def escolher_menu(opcao, database):
    if opcao == 1:
        criar_consulta(database)
        menu_principal(database)
    elif opcao == 2:
        pagar_consulta(database)
        menu_principal(database)
    elif opcao == 7:
        sair()


def menu_principal(database):
    try:
        print('1 - Nova consulta (agendamento)')
        print('2 - Pagar Consulta')
        print('3 - Cancelar consulta')
        print('4 - Agendar retorno')
        print('5 - Relatório de consultas realizadas no mês por médico')
        print('6 - Relatório de faturamento da clínica por mês')
        print('7 - Sair')
        opcao_escolhida = int(input('Opção escolhida: '))
        if opcao_escolhida < 1 or opcao_escolhida > 7:
            print('Opção inválida. Tente novamente.')
            menu_principal(database)
        escolher_menu(opcao_escolhida, database)
    except:
        print('Opção inválida. Tente novamente.')
        menu_principal(database)


def inicializa_database():
    # print("Inicializando database...")
    database = Database("dbpoo")

    medicoLucas = Medico('crm001', 'Lucas Rêgo')
    medicoKleber = Medico('crm002', 'Kléber Júnior')
    medicaBruna = Medico('crm003', 'Bruna Carla')
    clinicaIfpi = Clinica(
        '78561001000100', 'Clínica Instituto Federal do Piauí')
    clinicaUfpi = Clinica(
        '29045734000179', 'Clínica Universidade Federal do Piauí')

    # O médico Lucas atende pelo IFPI e pela UFPI
    medicoLucas.addClinica(clinicaIfpi)
    clinicaIfpi.addMedico(medicoLucas)
    medicoLucas.addClinica(clinicaUfpi)
    clinicaUfpi.addMedico(medicoLucas)

    # O médico Kléber atende pelo IFPI e pela UFPI
    medicoKleber.addClinica(clinicaIfpi)
    clinicaIfpi.addMedico(medicoKleber)
    medicoKleber.addClinica(clinicaUfpi)
    clinicaUfpi.addMedico(medicoKleber)

    # A médica Bruna atende apenas pelo IFPI
    medicaBruna.addClinica(clinicaIfpi)
    clinicaIfpi.addMedico(medicaBruna)

    # Adiciona no banco de dados as entidades acima
    database.addClinica(clinicaIfpi)
    database.addClinica(clinicaUfpi)
    database.addMedico(medicoLucas)
    database.addMedico(medicoKleber)
    database.addMedico(medicaBruna)

    # Exibe todas as clínicas
    # database.exibeTodasAsClinicas()

    # print("Database inicializado.")
    return database


if __name__ == "__main__":
    # Inicializa o banco com três médicos e duas clínicas
    database = inicializa_database()

    menu_principal(database)
