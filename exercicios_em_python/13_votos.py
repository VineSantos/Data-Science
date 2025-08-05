votos_candidato = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulos = 0
votos_branco = 0
total_votos = 0

while True:
    voto = int(input("Digite o voto (ou 0 para encerrar): "))
    
    if voto == 0:
        break
    
    if voto in votos_candidato:
        votos_candidato[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    
    total_votos += 1

print("Total de votos para cada candidato:")
for candidato, votos in votos_candidato.items():
    print(f"Candidato {candidato}: {votos} votos")

print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_branco}")

percentual_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
percentual_branco = (votos_branco / total_votos) * 100 if total_votos > 0 else 0

print(f"Percentual de votos nulos sobre o total de votos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco sobre o total de votos: {percentual_branco:.2f}%")

