# 8.	Implemente uma função que, dado um valor, retorne se esse valor pertence ou não a um vetor de inteiros. 

vetor = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

valor = int(input('Digite um valor: '))

if valor in vetor:
    print('O valor está no vetor!')
else:
    print('O valor não está no vetor!')