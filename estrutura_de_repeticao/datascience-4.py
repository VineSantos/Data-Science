# Peça para o usuário digitar valores numéricos representando as idades de participantes de uma pesquisa. A entrada deve continuar até que a pessoa digite "fim". Armazene todas as idades em uma lista e, ao final:
# Mostre todas as idades digitadas
# Mostre a média das idades
# Mostre a maior e a menor idade
idades = []

while True:
    entrada = input("Digite idade os participantes (ou '0' para encerrar): ")
    
    if entrada.lower() == '0':
        break
    idades.append(int(entrada))
    
if len(idades) > 0:
    media_idade = sum(idades) / len(idades)
    print(f"A média das idades é: {media_idade:.1f}")
else:
    print("Nenhuma idade foi digitada, não é possível calcular a média.")
    
qtt_idades = len(idades)

    
print (f"Todas as idades digitas: {idades}")
print (f"A média de idade é {media_idade}")
print (f"A menor nota informada foi {min(idades)}")
print (f"A maior nota informada foi {max(idades)}")
print (f"A quantidade de idades informadas {qtt_idades}")
