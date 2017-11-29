from datetime import datetime

now = datetime.now()
data_limite = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

data = str(input("Digite a data da entrega: "))
if data > data_limite:
    print("Data de entrega expirada")
else: 
    print("Questao enviada")