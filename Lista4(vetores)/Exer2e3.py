# 2.	Implemente uma função que retorne o maior elemento de um vetor de inteiros. 
# 3.	Implemente uma função que retorne o menor elemento de um vetor de inteiros. 

valores = []
negativos = 0

primeiro_valor = int(input(f'Digite 10 valores [1/10]: '))
valores.append(primeiro_valor)

maior = primeiro_valor
menor = primeiro_valor

for i in range (9):
    valor = int(input(f'Digite 10 valores [{i+2}/10]: '))
    valores.append(valor)
    
    if valor > maior:
        maior = valor
    else:
        if valor < menor:
            menor = valor
    
    
    if valor < 0:
        negativos += 1
        
print(f'\n{negativos} numeros negativos')
print(f'O maior elemento do vetor é {maior}')
print(f'O menor elemento do vetor é {menor}')

# ou
print(f'O maior elemento do vetor é {max(valores)}')
print(f'O menor elemento do vetor é {min(valores)}')