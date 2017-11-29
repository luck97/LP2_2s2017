
matriculas =[]

while 0 == 0:
    matricula = int(input("Digite 1 se quiser matricular-se em uma disciplina ou 0 para finalizar: "))
    if matricula == 0:
        print("Finalizado")
        break
    if matricula !=0:
        materia = str(input("Digite o nome da materia que deseja se matricular: "))
        if materia in matriculas:
            print("Você ja esta matriculado nessa disciplina !!")
            break
        else: 
            matriculas.append(materia)
