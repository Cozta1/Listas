salario = float(input("Seu salario: "))
financiamento = float(input("Financiamento: "))

if financiamento <= (salario * 5):
    print('Financiamento concedido!')
else:
    print('Financiamento negado!')