#Ler a idade e separar entre menor de idade, adulto e idoso
idade = int(input("Digita a idade: "))
if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")