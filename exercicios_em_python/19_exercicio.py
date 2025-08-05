# Solicita a palavra do usuario
palavra = input("Digite uma palavra: ")

# Remove espaços e transforma em minúscula para comparar corretamente
palavra_formatada = palavra.replace(" ", "").lower()

# Verifica se é palíndromo não
if palavra_formatada == palavra_formatada[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")