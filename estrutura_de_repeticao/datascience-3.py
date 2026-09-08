#7. Frase ao contrário
#Mostre a frase digitada de trás para frente.
frase = input("Digite uma frase: ")

palavras_invertidas = frase[::-1]
print(palavras_invertidas)

input ("aperte enter para continuar")

# 8. Frequência de letras
# Peça uma frase e uma letra.
# Conte quantas vezes a letra aparece, ignorando maiúsculas/minúsculas.
letra = input("Digite uma Letra: ")
frase = input("Agora vamos descobrir quantas dessa letra há na frase, digite uma frase: ")

letra = letra.lower()
frase = frase.lower()

frequencia = frase.count(letra)
print (f"A letra {letra} aparece {frequencia} na frase {frase}!")
input ("aperte enter para continuar")

# 9. Extrair iniciais
# Peça o nome completo.
# Extraia e mostre as iniciais, como: "João da Silva" → "J.S."
nomeCompleto = input("Digite seu nome completo")
palavras = nomeCompleto.split()

iniciais = [palavra[0].upper() for palavra in palavras]

resultado = '.'.join(iniciais) + '.'

print("Suas Iniciais:", resultado)




