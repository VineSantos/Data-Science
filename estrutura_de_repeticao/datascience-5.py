notas = [7.5, 8.0, 6.0, 9.2, 5.5, 8.8]

aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1
        
media = sum(notas) / len(notas)

print(f"{aprovados}")
print(f"{reprovados}")
print(f"{media}")

