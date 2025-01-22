
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:

    for i in range(1, numero + 1):
        fatorial *= i
        print (f"{numero} * {i} = {fatorial}")

    print(f"O fatorial de {numero} é {fatorial}")

    
