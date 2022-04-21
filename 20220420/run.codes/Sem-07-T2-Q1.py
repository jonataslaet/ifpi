def quantidadeTotalCaracteres(s, n):
    qtdCaracteres = len(n)

    if s == 1: 
        nomeDoConjuge = input().strip()
        qtdCaracteres = qtdCaracteres + len(nomeDoConjuge)
    print(qtdCaracteres)

if __name__ == "__main__":
    nome = input().strip()
    estadoCivil = int(input().strip())
    quantidadeTotalCaracteres(estadoCivil, nome)