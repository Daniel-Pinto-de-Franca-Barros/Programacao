#Ler um valor e se estiver fora de 0 a 100, mostrar o valor
num = float(input("Digite um número: "))
if num > 100 or num < 0:
    print("O número é", num)