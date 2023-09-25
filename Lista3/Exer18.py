num_perfeito = 0
numero = 1

while num_perfeito < 3:
    soma = 0
    numero+=1
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
            # print(i)
    
    if  soma == numero:
        num_perfeito += 1
        print(f'O numero {numero} é perfeito')
    numero += 1

# ESSE DEU UM TRABALHO DESGRACADO JUSUS CRISTO