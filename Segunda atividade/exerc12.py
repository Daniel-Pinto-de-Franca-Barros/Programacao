#Soma de dois números e mostrar se são iguais ou qual é maior
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
soma = num1 + num2
if num1 > num2:
    print("O número", num1,"é maior do que o número",num2)
elif num2 > num1:
    print("O número",num2,"é maior do que o número", num1)
else:
    print("O número", num1,"é igual ao", num2)