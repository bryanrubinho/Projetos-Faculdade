#9) Elaborar um programa que receba um número positivo e maior que zero, calcule e mostre:
#a) o número digitado ao quadrado;
#b) a raiz quadrada do número digitado;


import math
#entrada
n1= int(input("insira um valor maior que zero\n"))
#processo
raiz = math.sqrt(n1)
quadrado= math.pow(n1, 2)
#saida
print("o número digitado ao quadrado é:", quadrado)
print("A raiz do numero digitado é:", raiz)
