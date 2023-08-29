investido = float(input('$ INVESTIDO: '))
tempo = float(input('Tempo que o dinheiro está investido: '))

if tempo >= 5:
    print((investido + (investido * 0.095)) * tempo, '\n Juros de 0.95%')

else:
    if tempo >= 4:
        print((investido + (investido * 0.09))* tempo, '\n Juros de 0.90%' )

    else:
        if tempo >= 3:
            print((investido + (investido * 0.085)) * tempo, '\n Juros de 0.85%')

        else:
            if tempo >= 2:
                print((investido + (investido * 0.075))* tempo, '\n Juros de 0.75%')

            else:
                if tempo >= 1:
                    print((investido + (investido * 0.065))* tempo, '\n Juros de 0.65%')

                else:
                    if tempo < 1:
                        print((investido + (investido * 0.055))* tempo, '\n Juros de 0.55%')

                    else:
                        if tempo < 0:
                            print('Invalido')