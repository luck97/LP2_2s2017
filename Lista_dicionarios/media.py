def med(n1, n2):
    media = (n1+n2)/2
    return media

nome = "a"
while(nome != ""):

    nome  = str(input("Digite o nome do aluno: "))
    nota1 = int(input("Digite a primeira nota do aluno: "))
    nota2 = int(input("Digite a segunda nota do aluno: "))

    aluno = {
        nome : {
            nota1, nota2
        }
    }
    print("Aluno", nome,"media: ", med(nota1, nota2))