nasceu = int(input("Ano de nascimento: "))
atual = int(input("Ano atual: "))

idade = atual - nasceu

if idade >= 65:
    print('Idoso')

else:
    if idade >= 18:
        print('Adulto')

    else:
        if idade >= 12:
            print('Adolescente')

        else:
            if idade >= 4:
                print('Criança')

            else:
                if idade >= 0:
                    print('Bebe')