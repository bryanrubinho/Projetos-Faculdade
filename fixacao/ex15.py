#15) Elaborar um programa que leia três números inteiros (A, B, C) e calcule a seguinte expressão:
#D=R+S/2 onde R = (A + B)2 e S = (B + C)2. Exibir o valor D.

import math
#entrada
a= int(input("Insira o valor de A:\n"))
b= int(input("Insira o valor de B:\n"))
c= int(input("Insira o valor de C:\n"))
#processo
r= math.pow((a+b),2)
s= math.pow((b+c),2)
d=r+s/2
#saida
print("O valor de D é:\n", d)

