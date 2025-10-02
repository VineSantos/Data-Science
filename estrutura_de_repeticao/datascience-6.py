notas = []
pesos = []
interaçao = 1

while True:
    nota = int(input(f"Digite a {interaçao}ª nota: "))
    peso = int(input(f"Digite o peso da {interaçao}ª nota: "))
    
    interaçao += 1
    if peso == 0:
        break
    
    notas.append(nota)
    pesos.append(peso)
    
media_ponderada = sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)

print(f"Media ponderada: {media_ponderada:.2f}")
    