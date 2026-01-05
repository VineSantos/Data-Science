numero = int(input("Digite um número e diremos se ele é primo ou não: "))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, "não é primo!")
            break
    else:
        print(numero, "é primo!")
elif numero == 0:
    print(numero, " Valor digitado é 0")
elif numero == 1:
    print(numero, "Número digitado é 1. 1 não pode ser primo pois ele só pode ser dividido por ele mesmo")
else:
    print(numero, "Número negativo!")