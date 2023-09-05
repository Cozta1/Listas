nota = float(input('Nota: '))

if nota > 10 or nota < 0:
    print('Nota inválida')
else:
    if nota >= 9:
        print('Conceito A')
    else:
        if nota >= 7:
            print('Conceito B')
        else:
            if nota >= 5:
                print('Conceito C')
            else:
                print('Conceito D')