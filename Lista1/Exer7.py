def a():
    kwh = int(input("Quantidade de QuiloWatts consumido: "))

    final = (kwh * 0.12) * ((kwh * 0.12) * 0.18)

    print(f"Valor final com ICMS é igual á : R${final}")

if(__name__ == '__main__'):
    a()