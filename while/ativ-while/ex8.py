#8)Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchida
#pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o
#número 1 a repetição termina. Exibir no final todos os elementos da lista.

lista=[]

while True:

    n=int(input("Insira um numero inteiro, positivo e par:\n"))

    if (n % 2 == 0) and (n>0):
        lista.append(n)
    elif (n==1):
        print("Encerrando.")
        break
print("Os numeros Inteiros, positivos e pares sao:\n", lista)




