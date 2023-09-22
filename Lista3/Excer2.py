primeiro_valor = float(input("Digite o 1º valor: "))
maior = primeiro_valor
menor = primeiro_valor

for i in range(2, 21):
    valor = float(input(f"Digite o {i}º valor: "))
    
    if valor > maior:
        maior = valor
    
    if valor < menor:
        menor = valor

print(f"O maior valor é: {maior:.0f}")
print(f"O menor valor é: {menor:.0f}")
