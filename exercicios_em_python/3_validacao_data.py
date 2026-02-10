import datetime

def validar_data(data_str):
    try:
        data = datetime.datetime.strptime(data_str, '%d/%m/%Y')
        if data.year < 2000:
            return False
        else:
            return data
    except ValueError:
        return False

def main():
    # Pedindo a data de "início de projeto"
    while True:
        data_inicio_input = input("Digite a data de início do projeto no formato dd/mm/aaaa: ")
        
        data_inicio = validar_data(data_inicio_input)
        if data_inicio:
            break
        else:
            print("Data inválida. A data de início não pode ser anterior ao ano 2000.")

    # Pedindo a segunda data até que seja maior ou igual à data de "início de projeto"
    while True:
        data_fim_input = input("Digite a segunda data no formato dd/mm/aaaa: ")
        data_fim = validar_data(data_fim_input)
        if data_fim and data_fim >= data_inicio:
            break
        else:
            print("Data inválida. A data não pode ser anterior à data de início do projeto.")

    print("Data início do projeto:", data_inicio.strftime('%d/%m/%Y'))
    print("Data final do projeto:", data_fim.strftime('%d/%m/%Y'))

if __name__ == "__main__":
    main()