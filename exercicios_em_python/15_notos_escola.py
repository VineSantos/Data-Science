nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

conceito = None

if 9 <= media <= 10:
    conceito = 'A'
elif 7.5 <= media < 9:
    conceito = 'B'
elif 6 <= media < 7.5:
    conceito = 'C'
elif 4 <= media < 6:
    conceito = 'D'
else:
    conceito = 'E'

print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")

if conceito in ['A', 'B', 'C']:
    print("APROVADO")
else:
    print("REPROVADO")
