from Funcionario import Funcionario

nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
salarioOriginal = salario
funcionario = Funcionario(nome, salario)

aumento = int(input("Informe a porcentagem de aumento para o funcionário: "))

funcionario.aumentarSalario(aumento)

print("""
    O salário original de %s é %.2f
    com o aumento de %d por cento ficou %.2f
""" % (funcionario.nome, salarioOriginal, aumento, funcionario.salario))