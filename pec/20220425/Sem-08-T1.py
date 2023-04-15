# Remove os acentos do texto 
def remover_acentos(texto):
    from unicodedata import normalize

    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

# Fornece o signo de acordo com o dia e mês
def signo(dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gemeos'
    if mes == 6:
        return 'Gemeos' if dia < 22 else 'Cancer'
    if mes == 7:
        return 'Cancer' if dia < 23 else 'Leão'
    if mes == 8 :
        return 'Leão' if dia < 23 else 'Virgem' 
    if mes == 9 : 
        return 'Virgem' if dia < 23 else 'Libra' 
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio' 
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

# Fornece uma mensagem do horóscopo de acordo com o signo 
def horoscopo(signo_desejado):
    import urllib.request

    # Retorna o signo formatado: com os acentos removidos e tudo minúsculo
    signo_formatado = remover_acentos(signo_desejado).lower()

    # Concatena o signo formatado com a url
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    # Faz uma requisição à url anteriormente formatada
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    # Captura a resposta da requisição anteriormente feita
    resposta = urllib.request.urlopen(requisicao)

    # Captura a página da resposta anteriormente feita, e a decodifica em formato utf-8
    pagina = resposta.read().decode('utf-8')

    # Prepara dois marcadores de parágrafo: um de abertura e outro de fechamento, com uma classe definida no de abertura
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    # Prepara o início e o final de um texto de horóscopo
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    # Retorna o signo, um ponto, um espaço em branco e o texto do horóscopo do signo
    return signo_desejado + '. ' + pagina[inicio:final]

# Separa data em formato dia, mês e ano, respectivamente
def separar_data(dma):
    a = dma % 10000
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma
    return d, m, a

def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saída de dados
    print(horoscopo_de_hoje)

if __name__ == "__main__":
    main()