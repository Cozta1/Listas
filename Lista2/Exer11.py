horas = float(input("Horas trabalhadas: "))

if horas <= 40:
    print(horas * 15)
else:
    print((horas * 15) + (horas * 21) + 600)