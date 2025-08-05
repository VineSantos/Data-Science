lista = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes, Beatriz Costa, Felipe Almeida, Mariana Fernandes, João Pinto, Luísa Nascimento, Gabriel Souza, Manuela Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'

nome_1 = input("Digite o primeiro nome: ")
nome_2 = input("Digite o segundo nome: ")
nome_3 = input("Digite o terceiro nome: ")

nome_1 = nome_1.strip()
nome_2 = nome_2.strip()
nome_3 = nome_3.strip()

joao_na_lista = nome_1 in lista
vinicius_na_lista = nome_2 in lista
ana_na_lista = nome_3 in lista

if joao_na_lista and vinicius_na_lista and ana_na_lista:
    print(f'{nome_1}, {nome_2} e {nome_3} estão na lista')
elif joao_na_lista and vinicius_na_lista:
    print(f'{nome_1} e {nome_2} estão na lista, {nome_3} não está na lista')
elif joao_na_lista and ana_na_lista:
    print(f'{nome_1} e {nome_3} estão na lista, {nome_2} não está na lista')
elif vinicius_na_lista and ana_na_lista:
    print(f'{nome_2} e {nome_3} estão na lista, {nome_1} não está na lista')
elif joao_na_lista:
    print(f'{nome_1} está na lista, {nome_2} e {nome_3} não estão na lista')
elif vinicius_na_lista:
    print(f'{nome_2} está na lista, {nome_1} e {nome_3} não estão na lista')
elif ana_na_lista:
    print(f'{nome_3} está na lista, {nome_1} e {nome_2} não estão na lista')
else:
    print(f'{nome_1}, {nome_2} e {nome_3} não estão na lista')
