#4. Contar palavras
#Peça uma frase e conte quantas palavras ela tem.
frase = str(input("Digite uma frase para começar: "))

palavras = frase.split()
quantidade = len(palavras)
print(quantidade)

input ("Digite enter para continuar")

#5. Substituir palavras
#Substitua uma palavra específica por outra na frase digitada.
frase = frase.lower().replace('sim', 'nao')
print(frase)

input("Aperte enter para continuar")

# 6. Formatar texto
# Peça nome, sobrenome e profissão.
# Monte a frase: "Olá, [NOME] [SOBRENOME], você é um(a) [PROFISSÃO]."
# Exiba tudo em caixa alta.
nome = input("Digite seu nome para continuar: ")
profissao = input("Digite sua profissao para continuar: ")

print (f"OLÁ {nome.upper()} VOCÊ É UM {profissao.upper()}")