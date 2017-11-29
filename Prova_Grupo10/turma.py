class Turma:
    
    def __init__(self, max, nome):
        self.max = max
        self.nome = nome
        self.alunos = []
    
    def matricular(self, aluno):
        if len(self.alunos) < self.max:
            self.alunos.append(aluno)
            print("aluno matriculado com sucesso!")
        else:
            self.alunos.append(aluno)
            print("Número de alunos maior que o maximo")