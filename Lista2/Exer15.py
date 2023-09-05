num1 = int(input('1° Numero: '))
num2 = int(input('2° Numero: '))
num3 = int(input('3° Numero: '))
num4 = int(input('4° Numero: '))

if num1 < num2 and num1 < num3 and num1 < num4:
    print(f'O 1° numero é o menor:', num1)
else:
    if num2 < num3 and num2 < num4:
        print(f'O 2° numero é o menor:', num2)
    else:
        if num3 < num4:
            print(f'O 3° numero é o menor:', num3)
        else:
            print(f'O 4° numero é o menor:', num4)