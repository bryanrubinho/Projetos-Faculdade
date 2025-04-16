#Elaborar um programa que receba o raio e a altura de uma lata de óleo para calcular e
#apresentar o valor do volume desta lata, dado: V = π*r2*h.


#entrada
import math
r= float(input("Insira o raio:\n"))
a= float(input("Insira a altura:\n "))
#processo
r2= math.pow (r, 2)
pi= 3.1416
v= pi*r2*a
#saida
print("O Volume da lata é:\n", v)
