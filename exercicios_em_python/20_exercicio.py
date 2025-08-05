gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

compras_acima_3000 = sum(1 for valor in gastos if valor > 3000)

total_compras = len(gastos)
porcentagem = (compras_acima_3000 / total_compras) * 100

print(f"Total de compras acima de 3000: {compras_acima_3000}")
print(f"Porcentagem de compras acima de R$ 3000: {porcentagem:.2f}%")
