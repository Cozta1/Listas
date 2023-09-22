qtd = int(input("Quantos valores a serem lidos: "))

soma_total = 0
p = 0
n = 0

for i in range(qtd):
    num = float(input(f"Digite o {i + 1}º valor: "))
    
    soma_total += num
    
    if num >= 0:
        p += 1
    else:
        if num < 0:
            n += 1


media = soma_total / qtd

p100 = (p/qtd) * 100

n100 = (n/qtd) * 100

print(f'\nMedia dos numeros é {media}')
print(f'% de numeros positivos é {p100}%')
print(f'% de numeros negativos é {n100}%')


    