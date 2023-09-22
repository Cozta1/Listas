numero = int(input("Digite um número para calcular o fatorial: "))

resultado = 1

if numero >= 0:
    for i in range(1, numero+1):
        resultado *= i
else:
    print("O fatorial de números negativos não está definido.")


print(f"O fatorial de {numero} é {resultado}")
