nota = int(input("Digite sua nota: "))

if nota < 0 or nota > 100:
    print("NOTA INVALIDA")
else:
    if nota>= 60:
        print("Aprovado")
    else:
        print("Reprovado")