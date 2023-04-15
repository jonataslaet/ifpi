class Carro:
    
    nome = None
    ano = None
    cor = None
    veloc_max = None
    veloc_atual = None
    estado = None
    
    def __init__(self, nome, ano, cor, veloc_max, veloc_atual, estado):
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.veloc_max = veloc_max
        self.veloc_atual = veloc_atual
        self.estado = estado
        
    def parar(self):
        if (self.veloc_atual > 0.0):
            self.veloc_atual = 0.0
            print("O carro "+self.nome+" foi parado com sucesso")
        
    def ligar(self):
        if (self.estado == "desligado"):
            print("O carro "+self.nome+" já foi desligado")
        else:
            self.estado = "ligado"
            print("O carro "+self.nome+" foi ligado com sucesso")
    
    def desligar(self):
        if (self.estado == "desligado"):
            print("O carro "+self.nome+" já foi desligado")
        else:
            self.veloc_atual = 0.0
            self.estado = "desligado"
            print("O carro "+self.nome+" foi desligado com sucesso")
                
    def acelerar(self, velocidade_aumentada):
        if (self.estado == "desligado"):
            print("O carro "+self.nome+" só pode ser acelerado quando estiver ligado")
            
        elif (self.veloc_max < (velocidade_aumentada + self.veloc_atual)):
            print("O carro "+self.nome+" não pode ultrapassar a velocidade máxima")
            
        else:    
            self.veloc_atual = self.veloc_atual + velocidade_aumentada
            print("O carro "+self.nome+" foi acelerado com sucesso. Sua velocidade atual é " + str(self.veloc_atual))

if __name__ == "__main__":
    carro1 = Carro("Fusca", 1965, "Preto", 80.0, 20.0, "ligado")
    carro2 = Carro("Ferrari_sr2000", 2014, "Vermelho", 300.0, 0.0, "desligado")
    
    # a) Acelere o fusca para a velocidade: 40
    carro1.acelerar(40.0)
    
    # b) Acelere a ferrari para a velocidade: 200
    carro2.acelerar(200.0)
    
    # c) Desligue o fusca
    carro1.desligar()
    
    # d) Ligue a ferrari
    carro2.ligar()
    
    # e) acelere a ferrari para: 320
    carro2.acelerar(320.0)
    
    # f) Pare a ferrari.
    carro2.parar()
    
    # g) Desligue a ferrari
    carro2.desligar()
    
    # h) Ligue o fusca
    carro1.ligar()
    
    # i) Acelere o fusca para: 100
    carro1.acelerar(100.0)
    
    # j) Desligue o fusca
    carro1.desligar()