# 4.	Implemente uma função que ordene um vetor de inteiros de tamanho 10. 

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

# não sei fazer isso 🤷‍♂️
valores.sort()
print(valores)