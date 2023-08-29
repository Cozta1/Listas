prova1 = float(input("Digite a sua nota da primeira prova: "))
prova2 = float(input("Digite a sua nota da segunda prova: "))
trabalho = float(input("Digite a sua nota do trabalho: "))
faltas = float(input("Digite suas faltas: "))

media =  ((prova1 * 3) + (prova2 * 5) + (trabalho * 2))

if prova1 or prova2 or trabalho >10 or prova1 or prova2 or trabalho < 0:
     print("VALOR INVALIDO")

else:
    if faltas > 15:
        print("REPROVADO POR FALTAS\n", media)

    else:
        if media >= 60:
            print("Aprovado\n", media)

        else:
            print("REPROVADO, PROVA FINAL\n", media)