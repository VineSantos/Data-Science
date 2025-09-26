candidatos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
    }
votosbrancos = 0
votosnulos = 0

for i in range (0, 20):
    voto = int(input(f"Olá funcionário {i+1} vote em um dos 4 candidatos da sua preferência ou 5 - branco ou 6 - nulo!"))
    
    if voto in candidatos:
        candidatos[voto] += 1
    elif voto == 5:
        votosnulos += 1
    elif voto == 6:
        votosbrancos += 1
        
print("Total de votos para cada candidato: ")
for candidato, votos in candidatos.items():
    print(f"Candidato {candidato}: {votos} votos")

