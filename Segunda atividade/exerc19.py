#Ler dois números e mostrar a diferença entre eles se forem diferentes
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
diferenca = num1 - num2
if num1 != num2:
    print("A diferença entre", num1,"e",num2,"é",diferenca)
else:
    print("Os dois números são iguais")