list = []
for i in range(3):
    pessoa = {}
    
    pessoa["nome"] = input("Nome: ")
    pessoa["idade"] = int(input("Idade"))
    pessoa["cidade"] = input("Cidade: ")
    
    list.append(pessoa)
    
    profissao = {}
    
    profissao["endereço"] = input("Onde você mora? ")
    profissao["numero"] = int(input("Nº: "))
    
    list.append(profissao)
print(list)