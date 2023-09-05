salario = float(input("Seu salario: "))
tempo = float(input("Tempo de serviço: "))

if tempo <= 1:
    print(salario * 1.1)
else:
    print(salario * 1.2)