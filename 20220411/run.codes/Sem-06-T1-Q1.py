def mensagemDaPessoa(s, n):
    if sexo == 1: print("Ilmo Sr.", n)
    else: print("Ilma Sra.", n)

if __name__ == "__main__":
    nome = input().strip()
    sexo = int(input().strip())
    mensagemDaPessoa(sexo, nome)

