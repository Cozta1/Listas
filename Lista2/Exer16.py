codigo = int(input('Seu código: '))

if codigo > 106 or codigo < 101:
    print('Código inválido')
else:
    if codigo == 101:
        print('Cargo: Vendedor')
    else:
        if codigo == 102:
            print('Cargo: Atendente')
        else:
            if codigo == 103:
                print('Cargo: Auxiliar Técnico')
            else:
                if codigo == 104:
                    print('Cargo: Assistente')
                else:
                    if codigo == 105:
                        print('Cargo: Coordenador de Grupo')
                    else:
                        print('Cargo: Gerente')



# Cargo = ['Vendedor', 'Atendente', 'Auxiliar Técnico', 'Assistente', 'Coordenador de Grupo', 'Gerente']
#
# Codigo = int(input('Codigo: '))
#
# print(Cargo[Codigo - 101])