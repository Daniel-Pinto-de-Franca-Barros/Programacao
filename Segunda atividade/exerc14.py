#Converter para inteiro e ver se é ou não múltiplo de 3
num = float(input("Digite um número: "))
if num % 3 == 0:
    print("O", num,"é múltiplo de 3")
else:
    print("O", num,"Não é múltiplo de 3")