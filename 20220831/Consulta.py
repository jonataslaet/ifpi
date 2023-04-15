import string

import Clinica
import Medico


class Consulta:

    autorizacao: int
    medico: Medico
    clinica: Clinica
    valor: float
    dia: int
    mes: int
    ano: int
    status: string
    paga: bool
    quantidade: int = 0

    def __init__(self, clinica, medico, dia, mes, ano):
        self.autorizacao = Consulta.quantidade+1
        self.clinica = clinica
        self.medico = medico
        self.valor = 300.0
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.status = "CRIADO"
        self.paga = False
        Consulta.quantidade+=1

    def getStatus(self):
        return self.status

    def getMedico(self):
        return self.medico

    def getClinica(self):
        return self.clinica

    def getDia(self):
        return self.dia

    def getMes(self):
        return self.mes

    def getAno(self):
        return self.ano

    def getAutorizacao(self):
        return self.autorizacao

    def pagar(self):
        self.paga = True