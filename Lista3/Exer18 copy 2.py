num_perfeitos_encontrados = 0
numero = 2

while num_perfeitos_encontrados < 3:
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i

            
    if soma == numero:
        if num_perfeitos_encontrados == 0:
            print(f'O 1º número perfeito é: {numero}')
        elif num_perfeitos_encontrados == 1:
            print(f'O 2º número perfeito é: {numero}')
        else:
            print(f'O 3º número perfeito é: {numero}')
        num_perfeitos_encontrados += 1
    numero += 1
