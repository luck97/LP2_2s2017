class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentarSalario(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)