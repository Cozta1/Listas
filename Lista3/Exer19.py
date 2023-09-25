# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N! 

# num = int(input('Digite um número: '))

# for i in range(num):

#    fatorial = 1
#    for a in range(1, num + 1):
#        fatorial = fatorial * a


# print(f"O fatorial de {num} é {fatorial}")
   
   
num = int(input('Digite um número: '))
soma_final = 1

# for i in range (1, num + 1):
#     if num == 0:
#         print('Valor inválido, divisão por 0')
#     else:
        
fatorial = 1
for i in range(1, num + 1):
    fatorial = fatorial * i
    
    soma_final += 1/fatorial
    print(f'1/{fatorial}')
print(f'\nSoma total: {soma_final:.5f}')