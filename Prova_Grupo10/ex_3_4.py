alunos_enviaram = []
alunos_n_enviaram = []
codigo = 9874

while 0 == 0:
    print("Para cadastrar alunos que entregaram digite 1")
    print("Para cadastrar alunos que não entregaram digite 2")
    print("Para finalizar digite 0")

    codigo = int(input("Digite o codigo do cadastro: "))
    
    if codigo == 0:
        print("Encerrado")
        break

    if codigo == 1:
        print("Aluno que enviou")
        aluno = str(input("Digite o nome do aluno: "))
        alunos_enviaram.append(aluno)

    if codigo == 2:
        print("Aluno que não enviou")
        aluno = str(input("Digite o nome do aluno: "))
        alunos_n_enviaram.append(aluno)

print("Alunos que enviaram: ",alunos_enviaram)
print("Alunos que não enviaram",alunos_n_enviaram)

