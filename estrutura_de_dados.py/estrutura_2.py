ocorrencias = [
    "Roubo", "Furto", "Roubo", "Agressão",
    "Furto", "Furto", "Roubo", "Agressão"
    "Furto", "Furto", "Roubo", "Agressão"
]

contagem = {}

for item in ocorrencias:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1
        
for ocorrencias, quantidade in contagem.items():
    print(f"{ocorrencias}: {quantidade}")
    
mais_frequente = max(contagem, key=contagem.get)

print(f"Ocorrencis mais frenquente: {mais_frequente}({contagem[mais_frequente]})")