print("Vamos calcular a variação anual de vendas entre 2022 e 2023")

ano22 = int(input("Digite quantas vendas teve no ano de 2022: "))

ano23 = int(input("Digite quantas vendas teve no ano de 2023: "))

variacao_porcentual = ((ano23 - ano22) / ano22) * 100
variacao_formatada = round(variacao_porcentual, 2)


if variacao_porcentual > 20:
    print(f"Aumento de {variacao_porcentual}%!! Bonificação para toda equipe!")
elif 2 <= variacao_porcentual <= 20:
    print(f"Aumento de {variacao_porcentual}%!! Bonificação parcial para toda equipe")
elif -10 <= variacao_porcentual <= 2:
    print(f"Aumento de {variacao_porcentual}%!! planejamento de políticas de incentivo às vendas")
elif variacao_porcentual < -10:
    print(f"Variação de {variacao_porcentual}%!! Corte de gastos")
