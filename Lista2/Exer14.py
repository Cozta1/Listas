nome = input("Digite seu nome: ")

prova1 = float(input("Digite a sua nota da primeira prova: "))

if prova1 > 10 or prova1 < 0:
     print("VALOR INVALIDO")
else:
    prova2 = float(input("Digite a sua nota da segunda prova: "))

    if prova2 > 10 or prova2 < 0:
        print("VALOR INVALIDO")
    else:
        trabalho = float(input("Digite a sua nota do trabalho: "))

        if trabalho > 10 or trabalho < 0:
             print("VALOR INVALIDO")
        else:

            faltas = float(input("Digite suas faltas: "))

            if faltas < 0:
                 print("VALOR INVALIDO")

            else:
                media = ((prova1 * 3) + (prova2 * 5) + (trabalho * 2)) / 10

                if faltas > 15:
                    print(nome, "REPROVADO POR FALTAS\n", media)

                else:
                    if media >= 60:
                        print(nome, "Aprovado\n", media)

                    else:
                        print(nome, "REPROVADO, PROVA FINAL\n", media)

