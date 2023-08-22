def a():
    salario_bruto = float(input('Salario bruto: '))
    horas = int(input('Quantidade de horas extras: '))
    horas_valor = float(input('Valor recebido por hora extra: '))

    salario_liquido = (salario_bruto + (horas * horas_valor)) - ((salario_bruto + (horas * horas_valor))* 0.08)

    print(f'Seu salario liquido é de R$:{salario_liquido}')