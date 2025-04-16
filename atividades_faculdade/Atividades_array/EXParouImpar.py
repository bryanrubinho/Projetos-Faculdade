#4)Elaborar um algoritmo que lê 20 números inteiros. Para cada número inserido exibir se é par ou
#ímpar.
x= range(1, 21, 1)

for n in x :
    num= int(input("Insira um numero:\n"))

    if (num % 2 == 0):
        print("E par")
    else:
        print("Impar")
