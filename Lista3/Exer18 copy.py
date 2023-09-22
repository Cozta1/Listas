soma = 0
perfeito = 0


n = int(input('Digite um número: '))

for i in range(1, n + 1):
    
    if n % i == 0 :
        divisor = n / i
        soma += divisor
        print(divisor)
    
    if soma - n == n:
        perfeito += 1
        print(f'O numero {n} é perfeito')
