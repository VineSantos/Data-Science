notas = []

for i in range(15):
    while True:
        nota = int(input(f"Digite a nota {i+1}ª nota (0 a 5): "))
        if 0 <= nota <= 5:
            notas.append(nota)
            print("Nota válida")
            break
        else:
            print("Nota inválida, digite novamente!")