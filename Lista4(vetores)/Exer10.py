# 10.	Escrever uma função que substitui por zero todos os números negativos do vetor passado por parâmetro.

vetor = []

for i in range (5):
    valor = int(input(f'Digite um valor: '))
    if valor < 0:
        valor = 0
    vetor.append(valor)
    

print(vetor)