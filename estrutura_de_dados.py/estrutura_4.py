lista = []
for i in range(5):
    numero = int(input("Digite 5 números, e irei mostra-lo do maior para o menor: "))
    lista.append(numero)
    
    
lista.sort(reverse=True)
print(lista)
