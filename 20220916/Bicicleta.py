class Bicicleta:
    peso: float
    altura: float
    cor: str
    aro: float
    veloc_atual: float
    altura_cela: float
    calibragem_pneus: float


    def __init__(self, peso, altura, cor, aro, veloc_atual = 0.0, altura_cela = 0.0, calibragem_pneus = 20.0):
        self.peso = peso
        self.altura = altura
        self.cor = cor
        self.aro = aro
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus

def main():
    bicicleta1 = Bicicleta(5.0, 50.0, 'Vermelho', 40.0)
    bicicleta2 = Bicicleta(5.0, 50.0, 'Vermelho', 40.0, 15.0)
    print('Bicicleta 1 está a %.f km/h' %(bicicleta1.veloc_atual))
    print('Bicicleta 2 está a %.f km/h' %(bicicleta2.veloc_atual))


if __name__ == '__main__':
    main()