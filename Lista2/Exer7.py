salario = float(input("Seu salario: "))
tempo = float(input("Tempo de serviço: "))

if tempo <= 1:
    print(salario + (salario * 0.1))
if tempo > 1:
    print(salario + (salario * 0.2))

