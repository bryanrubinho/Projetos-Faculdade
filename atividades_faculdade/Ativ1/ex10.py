#10) Elaborar um programa que dados dois lados de um triângulo retângulo calcule e exiba a
#respectiva hipotenusa.

import math

#entrada
l1 = int(input("Insira o lado do triangulo retangulo\n"))
l2 = int(input("Insira o lado do triangulo retangulo\n"))
#processo
hipo= math.sqrt((l1*l1)+(l2*l2))
#saida
print("A hipotenusa é:", hipo)