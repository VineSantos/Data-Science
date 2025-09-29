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
        votosbrancos += 1
    elif voto == 6:
        votosnulos += 1

total_de_votos = sum(candidatos.values()) + votosbrancos + votosnulos

pctgem_votosbrancos = (votosbrancos / total_de_votos) * 100

pctgem_votosnulos = (votosnulos / total_de_votos) * 100


todas_as_opcoes = {
    "Candidato 1": candidatos[1],
    "Candidato 2": candidatos[2],
    "Candidato 3": candidatos[3],
    "Candidato 4": candidatos[4],
    "Brancos": votosbrancos,
    "Nulos": votosnulos
}

vencedor_geral = max(todas_as_opcoes, key=todas_as_opcoes.get)

print("Total de votos para cada candidato: ")
for candidato, votos in candidatos.items():
    print(f"Candidato {candidato}: {votos} votos")
    
print(f"Quantidade de votos em branco {votosbrancos}")
print(f"Quantidade de votos nulos {votosnulos}")
print(f"Porcentual de votos brancos: {pctgem_votosbrancos:.0f}%")
print(f"Porcentual de votos nulos: {pctgem_votosnulos:.0f}%")

if vencedor_geral == "Brancos":
    print(f"Não houve um candidato vencedor. Votos em branco foi maioria! Total: {votosbrancos}")
elif vencedor_geral == "Nulos":
    print(f"Não houve um candidato vencedor. Votos nulos foi maioria! Total: {votosnulos}")
else:
    print(f"Maior candidato foi: {vencedor_geral}")