import string

import Clinica
import Consulta


class Medico:

    crm: string
    nome: string
    consultas: Consulta
    clinicas: Clinica
    valorAcumuladoDasConsultas: float

    def __init__(self, crm, nome):
        self.crm = crm
        self.nome = nome
        self.consultas = []
        self.clinicas = []
        self.valorAcumuladoDasConsultas = 0

    def addClinica(self, clinica):
        self.clinicas.append(clinica)

    def getNome(self):
        return self.nome
