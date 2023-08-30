num1 = int(input('1° Numero: '))
num2 = int(input('2° Numero: '))
num3 = int(input('3° Numero: '))
num4 = int(input('4° Numero: '))

if num1 < num2 and num1 < num3 and num1 < num4:
    print('O 1° numero é o menor')
else:
    if num2 < num1 and num2 < num3 and num2 < num4:
        print('O 2° numero é o menor')
    else:
        if num3 < num1 and num3 < num2 and num3 < num4:
            print('O 3° numero é o menor')
        else:
            if num4 < num1 and num4 < num2 and num4 < num3:
                print('O 4° numero é o menor')