temperatura = []

while True:
    temp = int(input("Digite uma temperatura: "))
    ##print(f"{temp:.1f}ºC")
    if temp == -273:
        break
    temperatura.append(temp)
            
    if temperatura:
        media = sum(temperatura) / len(temperatura)
        print(f"A média das temperaturas foi {media:.0f}ºC")
    else:
        print("Nenhuma temperatura foi digitada.")
