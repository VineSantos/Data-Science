print ("E ai bora fazer um esprestimo consignado para financiar seu ap?")

valor = float(input("quanto é o ap que você pretende financiar?"))
salario = float(input("quanto você ganha por mês?"))
anos = int(input("quanto anos você pretende pagar?"))

prestação = valor / (anos * 12)
minimo = salario * 30 / 100
apdisponivel = minimo * (anos * 12)

print (f"a prestação do seu ap por mês será {prestação} e o max que voce poderá pagar referente0 a 30% do seu salario é de {minimo} ")


if prestação > minimo:
    print("Infelizmente não poderemos fazer o emprestimo para você pq o valor da prestação ultrapassa 30% do seu salário")
else:
    print("você poderá pagar o imprestimo")

print (f"O maximo que você irá conseguir em {anos} anos, com a renda mensal de R${salario: .0f} com 30% disso R${minimo: .0f} vai ser financiar um ap de R${apdisponivel: .0f}")