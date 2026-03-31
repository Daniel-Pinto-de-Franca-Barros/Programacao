#Informar a raiz se o número for positivo, caso contrário, número inválido
num = float(input("Digite um número: "))
if num >= 0:
    print("A raiz de", num,"é", num**0.5)
else:
    print("Número inválido")