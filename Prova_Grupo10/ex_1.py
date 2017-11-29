from alunos import alunos

for aluno in alunos:
    print("nome: " + aluno['nome'] )
    n1 = aluno['notas']['n1']
    n2 = aluno['notas']['n2']
    media = (n1 + n2)/2
    print("Media:",  media)
