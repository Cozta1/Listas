soma_par = 0
soma_impar = 0

par = 0
impar = 0

num = float(input(f"Digite um numero: "))

while num != 0:
    
    if num != 0:
        if num % 2 == 0:
            par += 1
            soma_par += num
        else:
            if num % 2 != 0:
                impar += 1
                soma_impar += num
                
    num = float(input(f"Digite um numero: "))

media_par = soma_par / par
media_impar = soma_impar / impar

print(f'\nO total de numeros pares é {par}')
print(f'O total de numeros impares é {impar}')

print(f'\nMedia dos numeros pares é {media_par}')
print(f'Media dos numeros impares é {media_impar}')

