num1 = int(input('1° Numero: '))
num2 = int(input('2° Numero: '))
codigo = int(input('Código: '))


if codigo > 3 or codigo < 1:
    print('Código inválido')
else:
    if codigo == 1:
        print(num1 + num2)
    else:
        if codigo == 2:
            print(num1 * num2)
        else:
            if codigo == 3:
                print(num1 / num2)