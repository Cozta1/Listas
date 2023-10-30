# 1.	Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores são 
# negativos

valores = []
negativos = 0
for i in range (10):
    valor = int(input('Digite 10 valores: '))
    valores.append(valor)
    if valor < 0:
        negativos += 1
print(f'\n{negativos} numeros negativos')
    


