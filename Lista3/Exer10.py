qtd = int(input("Quantos numeros para fatorar: "))

for i in range(qtd):

   num = int(input("Digite um numero para fatorar: "))

   fatorial = 1
   for a in range(1, num + 1):
       fatorial = fatorial * a


   print(f"O fatorial de {num} é {fatorial}")
