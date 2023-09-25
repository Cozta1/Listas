num = int(input('Digite um número: '))
soma_final = 1

fatorial = 1
for i in range(1, num + 1):
    fatorial = fatorial * i
    
    soma_final += 1/fatorial
    print(f'1/{fatorial}')
print(f'\nSoma total: {soma_final:.5f}')