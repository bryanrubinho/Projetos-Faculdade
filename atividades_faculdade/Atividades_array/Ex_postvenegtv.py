#2) Elaborar um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este
#número é múltiplo de 3 e se é positivo ou negativo. Esse programa deve-se repetir 6 vezes esse
#processo.

for x in range(1, 7, 1):
    n1= int(input("Insira um numero inteiro:\n"))

    if (n1>0):
        print("Positivo")
    elif (n1<0):
        print("Negativo")
    else:
        print("Invalido")

    if (n1 % 3 == 0):
        print ("O valor e divisivel por 3")
    else:
        print ("Nao divisivel por 3")


