votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulos = 0
votos_branco = 0

nomes_candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

while True:
    voto = int(input("Digite o código do candidato (ou 0 para encerrar): "))
    
    if voto == 0:
        break
    
    if voto in votos_candidatos:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1

print("Resultados da eleição:")
for codigo, votos in votos_candidatos.items():
    nome_candidato = nomes_candidatos[codigo]
    print(f"{nome_candidato}: {votos} votos")

print(f"Votos Nulos: {votos_nulos}")
print(f"Votos em Branco: {votos_branco}")

total_votos = sum(votos_candidatos.values()) + votos_nulos + votos_branco
percentual_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
percentual_branco = (votos_branco / total_votos) * 100 if total_votos > 0 else 0

print(f"Percentual de Votos Nulos sobre o total de votos: {percentual_nulos:.2f}%")
print(f"Percentual de Votos em Branco sobre o total de votos: {percentual_branco:.2f}%")
