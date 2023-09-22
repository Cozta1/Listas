qtd = 0
intervalo = 0

for i in range(10):
    num = int(input('Digite um número: '))
    qtd += 1
    if num >= 10 and num <= 20:
        intervalo+=1
print(f'{qtd} numeros totais, {intervalo} no intervalo de [10, 20] e {qtd - intervalo} fora')
        
    