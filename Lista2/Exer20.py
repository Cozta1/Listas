num1 = int(input('Digite um numero entre 1 e 10 valor: '))
num2 = int(input('Digite outro numero entre 1 e 10 valor: '))

if num1 < 1 or num1 > 10 or num2 < 1 or num2 > 10:
    print('Valor invalido')
else:
    if num1 + num2 > 8:
        if num1 > num2:
            print(num1 / num2)
        else:
            print(num2 / num1)
    else:
        if num1 + num2 == 8:
            print(num1 * num2)
        else:
            if num1 + num2 < 8:
                print((num1 + num2) / 2)