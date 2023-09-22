nota = float(input('Nota:'))

if nota > 100 or nota < 0:
    print('Valor invalido')

elif nota >= 60:
    print('Aprovado')
elif nota >= 40:
    print('Prova final')
elif nota < 40:
    print('Reprovado')