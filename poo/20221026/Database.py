import string

import Clinica
import Consulta
import Medico


class Database:
    nome: string
    clinicas: Clinica = []
    medicos: Medico = []
    consultas: Consulta = []

    def __init__(self, nome):
        self.nome = nome
        self.clinicas = []
        self.medicos = []
        self.consultas = []

    def getMedicos(self):
        return self.medicos

    def getClinicas(self):
        return self.clinicas

    def addConsulta(self, consulta):
        consulta.id = len(self.consultas)+1
        self.consultas.append(consulta)

    def addMedico(self, medico):
        self.medicos.append(medico)

    def addClinica(self, clinica):
        self.clinicas.append(clinica)

    def getNome(self):
        return self.nome

    def exibeTodasAsClinicas(self):
        for c in self.getClinicas():
            print(c.getNome())

    def getConsultas(self):
        return self.consultas