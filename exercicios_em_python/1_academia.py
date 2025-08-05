codigos = []
alturas = []
pesos = []

while True:
    codigo = input("Digite o código do cliente (ou 0 para encerrar): ")
    
    if codigo == '0':
        break
    
    altura = float(input("Digite a altura do cliente: "))
    peso = float(input("Digite o peso do cliente: "))

    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)

if len(codigos) > 0:
    indice_mais_alto = alturas.index(max(alturas))
    indice_mais_baixo = alturas.index(min(alturas))
    indice_mais_gordo = pesos.index(max(pesos))
    indice_mais_magro = pesos.index(min(pesos))

    print(f"Código do cliente mais alto: {codigos[indice_mais_alto]}, Altura: {alturas[indice_mais_alto]}, Peso: {pesos[indice_mais_alto]}")
    print(f"Código do cliente mais baixo: {codigos[indice_mais_baixo]}, Altura: {alturas[indice_mais_baixo]}, Peso: {pesos[indice_mais_baixo]}")
    print(f"Código do cliente mais gordo: {codigos[indice_mais_gordo]}, Altura: {alturas[indice_mais_gordo]}, Peso: {pesos[indice_mais_gordo]}")
    print(f"Código do cliente mais magro: {codigos[indice_mais_magro]}, Altura: {alturas[indice_mais_magro]}, Peso: {pesos[indice_mais_magro]}")

    media_alturas = sum(alturas) / len(alturas)
    media_pesos = sum(pesos) / len(pesos)
    print(f"Média de alturas dos clientes: {media_alturas}")
    print(f"Média de pesos dos clientes: {media_pesos}")
else:
    print("Nenhum cliente cadastrado.")
