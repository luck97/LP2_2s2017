class Aluno:
    def __init__(self,nome, media, data):
        self.nome = nome
        self.media = media
        self.data = data

aluno1 = Aluno('felipe', 8, '11/12/2017')
aluno2 = Aluno('matheus', 8, '11/11/2017')
aluno3 = Aluno('taina', 10, '08/09/2017')
aluno4 = Aluno('lucas', 5, '13/07/2017')
aluno5 = Aluno('jonas', 7, '11/05/2017')

alunos = [
    aluno1,
    aluno2,
    aluno3,
    aluno4,
    aluno5
]

alunos = sorted(alunos, key=lambda aluno: aluno.data)
alunos = sorted(alunos, key=lambda aluno: aluno.media, reverse=True) 


for aluno in alunos:
    print("nome:",aluno.nome)
    print("media:",aluno.media)
    print("data matricula:",aluno.data)