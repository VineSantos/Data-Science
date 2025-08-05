import random
import time


while True:
    print("Ta afim de começar um RPG Surpreendente?")
    input("Pressione Enter para CONTINUAR >>")
    print(">>>>> Sim - 1 \n>>>>> Não - 2")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Ótimo! Vamos começar o RPG!")
        
        print("Você se encontra em uma floresta misteriosa. O que você faz?")
        print(">>>>> 1 - Pede por ajuda")
        print(">>>>> 2 - Tenta retornar para vila")
        print(">>>>> 3 - Explorar a floresta")
        acao = input("Escolha sua ação: ")
        
        if acao == "1":
            print(">>>>> Você começa a explorar a floresta e encontra um tesouro!")
        elif acao == "2":
            print(">>>>> Você volta para a vila e encontra um velho sábio.")
            print(">>>>> O velho te examina de cima a baixo\n")
            print("O que você diz?")
            print(">>>>>> 1 - Quem é você?")
            print(">>>>>> 2 - O que você faz aqui?")
            print(">>>>>> 3 - Ignora o homem")
            velho = input("Escolha uma opção: ")
            
            if velho == "1":
                print(">>>>> 1 - O velho responde: \n- Eu sou o mago dos magos, aquele e único")
            if velho == "2":
                print(">>>>> 2 - Eu vim atrás de um fruto proíbido, você sabe de algo?")
            else:
                print(">>>>> 3 - Voocê segue até sua cabana e o homem aparece novamente.")
            
        elif acao == "3":
            print(">>>>> Você encontra um fruto proíbido, o que faz?")
            print(">>>>> 1 - Eu como o fruto o que pode acontecer de errado?")
            print(">>>>> 2 - Você examina o fruto e guarda na sua bolsa")
            print(">>>>> 3 - Você ignora o fruto e continua sua jornada")
            fruto = input("escolha uma opção: ")
                
            if fruto == "1":
                print("o fruto estava envenenado!")
            elif fruto == "2":
                print("Esse fruto pode ser perigoso, melhor deixar para outra ocasião!")
            elif fruto == "3":
                print("Você se depara com um portal")
                print(">>>>> Para seguir nesse portal será necessário lançar 3 moedas. Cada moeda com valor de 0 à 9 e a soma dessas moeda precisar ser maior ou igual a 15.")
                print(">>>>> Pegue uma moeda")
                # ##input("Aperte Enter para lançar 1ª Moeda")
                # ##moeda1 = random.randint(0,9)
                # print(f"Resultado da 1ª moeda: {moeda1}")
                # ##input("Aperte Enter para lançar 2ª Moeda")
                # ##moeda2 = random.randint(0,9)
                # print(f"Resultado da 2ª moeda: {moeda2}")
                # ##input("Aperte Enter para lançar 3ª Moeda")
                # ##moeda3 = random.randint(0,9)
                # print(f"Resultado da 3ª moeda: {moeda3}")
                
                # resultado_moeda = moeda1 + moeda2 + moeda3
                
                contador = 1
                total_de_moedas = 4
                soma_moedas = 0
                
                while contador < total_de_moedas:
                    
                    moeda = random.randint(0,9)
                    print(f"Resultado da {contador}ª foi de {moeda}")
                    soma_moedas +=  moeda
                    contador += 1
                
                if soma_moedas >= 15:
                    print(f"O resultado da suas tentavas foram: {soma_moedas}\n Pode entrar pelo portal, e boa sorte!")
                else:
                    print("Tente novamente :-(")
            else:
                print("opção inválidade. Tente novamente.")
                
        else:
            print("Opção inválida. Tente novamente.")
        break
    
    elif escolha == "2":
        print("Tudo bem, vamos tentar novamente.")
        
    else:
        print("Opção inválida. Tente novamente.")
