#Informar se o número é par positivo, par negativo ou impar
num = float(input("Digite um número: "))
if num % 2 == 0 and num >= 0:
    print("O número é par e positivo")
elif num % 2 == 0 and num < 0:
    print("O número é par e negativo")
else:
    print("O número é impar")