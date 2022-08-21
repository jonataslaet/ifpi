from random import randint
from typing import Final

sexos_possiveis: Final[str] = ['M', 'F']


class Gato:

    nome = None
    fertil = None
    cio = None
    prenhe = None
    puerperio = None
    peso = None
    idade = None
    sexo = None
    filhos = None
    pai = None
    mae = None

    def __init__(self, nome, fertil, cio, prenhe, puerperio, peso, idade, sexo):
        self.nome = nome
        self.fertil = fertil
        self.cio = cio
        self.prenhe = prenhe
        self.puerperio = puerperio
        self.peso = peso
        self.idade = idade
        self.sexo = sexo
        self.filhos = []

    def engordar(self, peso_ganho):
        self.peso = self.peso + peso_ganho
        print("O gato "+self.nome+" engordou " + str(peso_ganho) +
              " kg, e agora seu peso é " + str(self.peso) + " kg.")

    def envelhecer(self):
        self.idade = self.idade + 1
        print('Eu, ' + self.nome + ', completo hoje ' +
              str(self.idade)+' anos de idade.')

    def entrar_no_cio(self):
        if (self.idade >= 1):
            self.cio = True
            print(self.nome + ' entrou no cio.')
        else:
            print('Apenas gatos com 1 ano ou mais podem entrar no cio.')

    def sexos_opostos(self, outro_gato):
        return self.sexo != outro_gato.sexo

    def retornar_gato_e_gata(self, outro_gato):
        if (self.sexo == 'M'):
            return self, outro_gato
        return outro_gato, self

    def parir(self):
        if (self.sexo == 'F' and self.prenhe == True):
            pai = self.filhos[-1].pai
            self.prenhe = False
            self.puerperio = True
            print(self.nome + ' pariu os seguintes filhos com o ' + pai.nome + ':')
            f = 1
            for filho in self.filhos:
                if (filho.pai == pai):
                    print('Filho ' + str(f) + ' com o ' +
                          pai.nome + ': ' + filho.nome)
                    f += 1
        else:
            print(self.nome + ' não pode parir.')

    def cruzar(self, outro_gato):
        gato_macho, gata_femea = self.retornar_gato_e_gata(outro_gato)
        if (not self.sexos_opostos(outro_gato)):
            print('O sexo dos gatos devem ser opostos para o cruzamento.')
        elif (gata_femea.cio == False):
            print('A fêmea deve estar no cio.')
        else:
            gata_femea.prenhe = True
            gata_femea.geraFilhos(gato_macho)
            print(self.nome + ' e ' + gato_macho.nome + ' cruzaram.')

    def tem_filho_de(self, outro_gato):
        for filho in self.filhos:
            if (filho in outro_gato.filhos):
                print('Eu, ' + self.nome + ', tenho filho de ' +
                      outro_gato.nome + '. O nome dele é ' + filho.nome + '.')
                return True
        print('Eu, ' + self.nome + ', não tenho filho de ' + outro_gato.nome + '.')
        return False

    def quantidadeFilhosGerada(self):
        if (self.sexo.upper() == 'M'):
            return 0
        maxFilhos = randint(0, 10)
        quantidadeGerada = randint(0, maxFilhos)
        return quantidadeGerada

    def meusFilhosComDeterminadoGato(self, gato_pai):
        filhos = []
        print('Eu, ' + self.nome +
              ', tenho os seguintes filhos com o ' + gato_pai.nome + ': ')
        for filho in self.filhos:
            if (filho.pai == gato_pai):
                filhos.append(filho)
        return filhos

    def geraFilhos(self, gato_pai):
        q = self.quantidadeFilhosGerada()
        if (self.sexo.upper() == 'F' and self.prenhe == True):
            for i in range(0, q+1):
                filhoGerado = Gato("Filho de " + str(
                    self.nome) + " e " + str(gato_pai.nome), False, False, False, False, 2.0, 0, sexos_possiveis[randint(0, 1)])
                filhoGerado.pai = gato_pai
                filhoGerado.mae = self
                self.filhos.append(filhoGerado)
                gato_pai.filhos.append(filhoGerado)


if __name__ == "__main__":
    bambino = Gato("Bambino", False, True, False, False, 2.0, 3, 'M')
    bambina = Gato("Bambina", True, False, False, False, 2.0, 3, 'F')
    bambinao = Gato("Bambinao", True, True, False, False, 2.0, 3, 'M')

    # a) Bambino tenta cruzar com o Bambinao
    bambino.cruzar(bambinao)

    # b) Bambino cruza com a Bambina quando ela não está no cio
    bambino.cruzar(bambina)

    # c) Bambina entra no cio
    bambina.entrar_no_cio()

    # d) Bambino cruza com a Bambina quando ela está no cio
    bambino.cruzar(bambina)

    # e) Bambina fica preenhe de Bambino
    bambino.tem_filho_de(bambina)

    # f) Bambina pariu
    bambina.parir()

    # g) Bambino engorda 1 kg
    bambino.engordar(1.0)

    # h) Bambino envelhece 1 ano
    bambino.envelhecer()

    # i) Bambinao não tem filho de Bambina
    bambinao.tem_filho_de(bambina)
