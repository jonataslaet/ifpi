import string

import Consulta
import Medico


class Clinica:

    nome: string
    cnpj: string
    medicos: Medico
    consultas: Consulta

    def __init__(self, cnpj, nome):
        self.nome = nome
        self.cnpj = cnpj
        self.medicos = []
        self.consultas = []

    def addMedico(self, medico):
        self.medicos.append(medico)

    def getMedicos(self):
        return self.medicos

    def getNome(self):
        return self.nome
