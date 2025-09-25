idades = []
jovem = []
adulto = []
meiaidade = []
idosos = []

while True:
    entrada = input("Digite sua idade: ")

    if entrada.lower() == 'x':
        print("Programa encerrado!")
        break
    
    try:
        idade = int(entrada)
        idades.append(idade)
                
        if 0 <= idade <= 25:
            jovem.append(idade)
            print("Você é jovem!")
        elif 26 <= idade <= 50:
            adulto.append(idade)
            print("Você é um adulto!")
        elif 50 <= idade <= 75:
            meiaidade.append(idade)
            print("Você está na meia idade!")
        elif 76 <= idade <= 100:
            idosos.append(idade)
            print("Você já um idoso!")
        else:
            print("Idade fora do intervalo permitido")
        
        print("\nDistribuição de idades:")
        print(f"0-25 anos: {jovem}")
        print(f"26-50 anos: {adulto}")
        print(f"51-75 anos: {meiaidade}")
        print(f"76-100 anos: {idosos}")

    except ValueError:
        print("Por favor, digite apenas números!")

