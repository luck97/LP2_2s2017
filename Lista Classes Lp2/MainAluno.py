from Aluno import Aluno

nome = input("Nome do aluno: ")
curso = input("Nome do Curso: ")
horasSemDormir = int(input("Quantidades de horas sem dormir: "))
horasDeEstudos = int(input("Quantidades de horas de estudo: "))
dormir = int(input("Quantidades de horas sono: "))

aluno = Aluno(nome, curso, horasSemDormir)
aluno.estudar(horasDeEstudos)
aluno.dormir(dormir)

print("%s esta %d horas sem dormir" % (aluno.nome, aluno.tempoSemDormir))