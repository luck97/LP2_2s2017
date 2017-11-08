class Aluno():
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
    
    def estudar(self, horas):
        self.tempoSemDormir += horas
    
    def dormir(self, horas):
        self.tempoSemDormir -= horas
