# A = [0,25]
# B = [26,50]
# C = [51,75]
# D = [76,100]

A = 0
B = 0
C = 0
D = 0

num = float(input("Digite um numero: "))

while num >= 0:
    if num >= 0 and num <= 25:
        A += 1
    else:
        if num >= 26 and num <= 50:
            B += 1
            
        else:
            if num >= 51 and num <= 75:
                C += 1
                
            else:
                if num >= 76 and num <= 100:
                    D += 1
                    
                else:
                    if num > 100:
                        print('Valor invalido')
                        

    num = float(input("Digite um numero: "))
    
print(f'A quantidade de valores no Grupo A é de {A}')
print(f'A quantidade de valores no Grupo B é de {B}')
print(f'A quantidade de valores no Grupo C é de {C}')
print(f'A quantidade de valores no Grupo D é de {D}')