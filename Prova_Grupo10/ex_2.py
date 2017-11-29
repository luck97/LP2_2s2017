from alunos import alunos

for aluno in alunos:
    print("nome: " + aluno['nome'] )

    if aluno['fez_teste']:
        print("Teste já realizado")
    else:
        print("Aplicar teste")