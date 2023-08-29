peso = float(input('Peso do carro: '))
ano = int(input('Ano do carro: '))

if ano >= 1980 and peso >= 1600:
    print('Automóvel de classe 8\nTaxa de registro: 55.50$')

else:
    if ano >= 1980 and peso < 1600:
        print('Automóvel de classe 7\nTaxa de registro: 19.50')

    else:
        if ano >= 1971 and peso > 1700:
            print('Automóvel de classe 6\nTaxa de registro: 52.50$')

        else:
            if ano >= 1971 and peso > 1200:
                print('Automóvel de classe 5\nTaxa de registro: 30.50$')

            else:
                if ano >= 1971 and peso < 1200:
                    print('Automóvel de classe 4\nTaxa de registro: 27.00$')

                else:
                    if ano <= 1970 and peso > 1700:
                        print('Automóvel de classe 3\nTaxa de registro: 46.50$')

                    else:
                        if ano <= 1970 and peso > 1200:
                            print('Automóvel de classe 2\nTaxa de registro: 25.50$')

                        else:
                            if ano <= 1970 and peso < 1200:
                                print('Automóvel de classe 1\nTaxa de registro: 16.50$')