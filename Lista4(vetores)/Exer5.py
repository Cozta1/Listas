# 5.	Escrever uma função que recebe por parâmetro um vetor de inteiros e retorna a soma de seus elementos. 

valores = []
soma = 0 
for i in range (5):
    valor = int(input(f'Digite um valor: '))
    valores.append(valor)
    soma += valor

print(soma)
# ou assim, mais rapido⚡
print(sum(valores))