while True:
    try:

        tabu = int(input("Digite um número que você gostaria que fosse mostrado a tabuada de 1 a 10: "))
        
        for i in range(1, 11):
            resul = tabu * i
            print(f"A tabuada de {tabu} x {i} = {resul}")


    except ValueError:
        print("Erro 'Apenas números inteiros são permitidos. Tente novamente")
        print("Até mais")