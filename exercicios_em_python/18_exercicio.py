idades = []
while True:
    entrada = input("Digite uma idade (ou -1 para sair): ")
    
    try:
        idade = int(entrada)
        if idade == -1:
            break
        elif idade < 0:
            print("Idade inválida! Tente novamente.")
        else:
            idades.append(idade)
    except ValueError:
        print("Por favor, digite um número válido.")

# Verifica se a lista não está vazia
if idades:
    menores_de_idade = sum(1 for idade in idades if idade < 18)
    media_idades = sum(idades) / len(idades)

    print(f"\nTotal de pessoas menores de idade: {menores_de_idade}")
    print(f"Idade média do grupo: {media_idades:.2f} anos")
else:
    print("Nenhuma idade foi informada.")
