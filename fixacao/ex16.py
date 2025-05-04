#16)Elaborar um programa que leia 3 notas de um aluno e calcule a média final deste aluno.
#Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.

import math as m
#entrada
n1= int(input("Insira a primeira nota\n:"))
n2= int(input("Insira a segunda nota:\n"))
n3= int(input("Insira a terceira nota:\n"))
#processo
n1= n1*2
n2= n2*3
n3= n3*5
media= n1+n2+n3/10
#saida
print("A média ponderada é:\n", media)