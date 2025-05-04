#3) Elaborar um algoritmo que recebe 3 valores (A, B e C) e exibe qual é o maior entre eles. Esse
#programa deve-se repetir 20 vezes.

n = range(1, 21, 1)
for x in n :

    a= int(input("Insira o valor A:\n"))
    b= int(input("Insira o valor B:\n"))
    c= int(input("Insira o valor C:\n"))

    if (a>b and a>c):
        print("O valor A e o maior!!")  
    elif (b>a and b>c):
        print("O valor B e o maior!!") 
    elif (c>a and c>b):
        print("O valor C e o maior!!") 
    else:
        print("Invalido!!!")