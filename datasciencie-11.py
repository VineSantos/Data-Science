idades = []
while True:
    entrada = input("Digite sua idade: ")

    if entrada.lower() == 'x':
        print("Programa encerrado!")
        break
    
    try:
        idade = int(entrada)
        idades.append(idade)
                
        if 0 <= idade <= 25:
            print("Você é jovem!")
        elif 26 <= idade <= 50:
            print("Você é um adulto!")
        elif 50 <= idade <= 75:
            print("Você está na meia idade!")
        elif 76 <= idade <= 100:
            print("Você já um idoso!")
        else:
            print("Idade fora do intervalo permitido")
        
        
    except ValueError:
        print("Por favor, digite apenas números!")