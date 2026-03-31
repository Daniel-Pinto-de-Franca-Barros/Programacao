#Ler um valor e mostrar o tipo, se for numérico, mostrar o quadrado
valor = input("Digite um valor: ")
try:
    num = float(valor)
    print("É numérico")
except:
    print("Não é numérico")
print("O tipo é", type(valor))
