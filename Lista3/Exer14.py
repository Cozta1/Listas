qtd = 0
soma_inicial = 0
soma_aumento = 0


cod = int(input('Digite o código do produto: '))

while cod >= 0:
    preco_inicial = float(input('Digite o preço do produto: '))
    
    preco_aumento = preco_inicial * 1.2
    
    print(f'\nCódigo: {cod}')
    print(f'Preço inicial: R$:{preco_inicial:.2f}')
    print(f'Preço com aumento: R$:{preco_aumento :.2f}  \n')
    
    soma_inicial += preco_inicial
    soma_aumento += preco_aumento
    qtd += 1
    
    cod = int(input('Digite o codigo do produto: '))
    
media_inicial = soma_inicial/qtd
media_aumento = soma_aumento/qtd
    
print(f'Média dos preços iniciais: R$:{media_inicial:.2f}')
print(f'Média dos preços com aumento: R$:{media_aumento:.2f}\n')