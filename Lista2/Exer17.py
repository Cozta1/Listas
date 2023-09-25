codigo = int(input('Código do disco: '))

if codigo > 4 or codigo < 1:
    print('Código inválido')
else:
    if codigo == 1:
        print('Tipo da unidade: CD-ROM (700MB)')
    else:
        if codigo == 2:
            print('Tipo da unidade: DVD-ROM (4.7GB)')
        else:
            if codigo == 3:
                print('Tipo da unidade: DVD-9 (8.54 GB)')
            else:
                print('Tipo da unidade: Blu-Ray (25 GB)')
