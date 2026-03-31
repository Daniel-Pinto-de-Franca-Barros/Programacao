#Mostrar se o número é par positivo, par negativo, impar positivo, impar negativo ou neutro
num = float(input("Digite um número: "))
if num % 2 == 0 and num >= 0:
    print("É par e positivo")
elif num % 2 == 0 and num < 0:
    print("É par e negativo")
elif num % 2 != 0 and num >= 0:
    print("É impar e positivo")
elif num % 2 != 0 and num < 0:
    print("É impar e negativo")
else:
    print("Neutro")