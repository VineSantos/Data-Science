notas = []
posicao = 0

for i in range(15):
    while True:
        nota = int(input("Digite uma nota: "))
        if nota < 0 or nota > 5:
            print("Digite uma nota entre 0 a 5")
        else:
            notas.append(nota)
            break
        
print("Notas inseridas:")
for nota in notas:
    print(f"A {posicao}ª nota foi:{nota}")
    posicao += 1