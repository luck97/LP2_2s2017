from Triangulo import Triangulo

ladoA = int(input("Informe o lado A do triângulo: "))
ladoB = int(input("Informe o lado B do triângulo: "))
ladoC = int(input("Informe o lado C do triângulo: "))

triangulo = Triangulo(ladoA, ladoB, ladoC)
perimetro = triangulo.calcularPerimetro()
maiorLado = triangulo.getMaior()

print("""
    O perímetro do Triângulo é %d
    O maior lado é %d
""" % (perimetro, maiorLado))
