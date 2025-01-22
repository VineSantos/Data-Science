print("Vamos descobrir quantos e quais números tem entre o 1º e o 2º?")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    for i in range (num1 + 1, num2):
        print(i)
elif num1 > num2:
    for i in range  (num2 + 1, num1):
        print(i)
else:
    print("Não há números inteiro entre os dois números fornecidos")