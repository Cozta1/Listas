def a():
    salario_base = float(input('Digite seu salario atual: '))
    aumento = float(input('Digite a porcentagem de aumento a ser recebido: '))

    salario_final = salario_base + (salario_base * (aumento/100))
    print(f'Seu salario final com aumento de {aumento:.1f}% é de {salario_final:.2f}')