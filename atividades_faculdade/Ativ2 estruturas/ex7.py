#7)Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais devera se 
#somar os dois, caso contrario multiplique A por B. Ao final de qualquer um dos cálculos deve-se 
#atribuir o resultado para uma variável C e mostrar seu conteudo na tela.


a= int(input("Insira o Valor a:\n"))
b= int(input("Insira o Valor b:\n"))

if (a == b):
    c= a+b
    print("A soma é:\n", c)
else:
    c=a*b
    print("A multiplicação é:\n", c)
