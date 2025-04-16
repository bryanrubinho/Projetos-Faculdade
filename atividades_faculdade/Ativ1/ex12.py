#12)Elaborar um programa que receba o raio de uma esfera. O algoritmo deve calcular e exibir a
#área e o volume da esfera.


import math as m
#entrada
pi=3.1416
r= float(input("Insira o Raio:\n"))
#processo
v= (4/3)*pi*m.pow(r, 3)
#saida
print("O volume é", v)