# 1. Maiúsculas e Minúsculas
# Peça para o usuário digitar uma frase.
# Exiba a frase toda em maiúsculas.
#Exiba a frase toda em minúsculas.
str1 = str(input("Digite uma frase:"))

input("Pressione Enter para continuar...")
print(f"A frase digitada foi: {str1}")
input("Pressione Enter para continuar...")

str1 = str1.lower()
print(str1)

input("Pressione Enter para continuar...")

str1 = str1.upper()
print(str1)

input("Enter para continuar")

# 2. Remoção de espaços
# Peça uma frase com espaços antes e depois.
# Remova os espaços desnecessários e exiba a frase limpa.
str1 = str1.strip()
print (str1)

input('Enter para continuar')

# 3. Verificar se começa ou termina com determinada palavra
# Verifique se a string começa com "Olá"
# Verifique se termina com "dados"
str1 = str1.lower().replace('e','A')

print (str1)
print(str1.startswith("dado"))
print(str1.endswith("tchau"))

input('Enter para continuar')

#split transforma uma string em lista, por isso é necessário armazenar em outra var
palavras = str1.split()
print(palavras)

