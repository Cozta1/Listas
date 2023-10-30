# 7.	Escrever a função que recebe por parâmetro uma string e um caracter. e a função deve retornar os primeiros caracteres da string até encontrar o caracter passado por parâmetro. 

string = input('Digite uma string: ').upper()

caracter = input('Digite um caracter presente na string: ').upper()


letra = ''

for char in string:

    if char == caracter:
        break
    
    letra += char

print(letra + caracter)
