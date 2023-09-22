perfeito1 = 0

numero = 1

while perfeito1 < 3:
    soma = 0
    for i in range(1, numero + 1):
        
        if numero % i == 0:
            # soma += i
            divisor = numero / i
            soma += divisor
            print(divisor)
            
        perfeito = soma - numero == numero
        if  perfeito:
            perfeito1 += 1
            print(f'O numero {numero} é perfeito')
        numero += 1    
        

       
        
        
        
#         if soma == numero:
#     if num_perfeitos_encontrados == 0:
#         print(f'O 1º número perfeito é: {numero}')
#     elif num_perfeitos_encontrados == 1:
#         print(f'O 2º número perfeito é: {numero}')
#     else:
#         print(f'O 3º número perfeito é: {numero}')
#     num_perfeitos_encontrados += 1
# numero += 1



