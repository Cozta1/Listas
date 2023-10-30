# 9.	Implemente uma função que retorne a média dos valores armazenados em um vetor de inteiros. 

vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
soma=0
qtd=0

for numero in vetor:
    soma+=numero
    qtd+=1
    
media = soma/qtd
print(media)