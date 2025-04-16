#1)Elaborar um algoritmo que leia um valor de temperatura em graus Celsius, calcule e exiba a
#temperatura equivalente em Kelvin, sabendo que: K = C + 273. Esse algoritmo deve repetir 5 vezes.

for x in range(1, 6, 1):
    c= int(input("Insira a temperatura em graus celcius:\n"))
    k= c+273
    print("A temperatura em Kelvin e:\n", k)
