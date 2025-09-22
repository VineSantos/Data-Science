print("Vamos calcular a variação anual de vendas entre 2022 e 2023")

ano22 = int(input("Digite quantas vendas teve no ano de 2022: "))

ano23 = int(input("Digite quantas vendas teve no ano de 2023: "))

variacao_porcentual = ((ano22 - ano23) / ano22) * 100

print(f"{variacao_porcentual}")