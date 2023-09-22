n = int(input('Digite um número: '))
S = 0
for i in range (1, n+1):
    if n == 0:
        print('Valor inválido, divisão por 0')
    else:
        s = 1/i
        S += s 
        print(f'1/{i}')
print(f'\nSoma total: {S}')