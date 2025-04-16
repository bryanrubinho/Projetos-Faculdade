#8)Elaborar um programa que leia três números inteiros positivos e efetue o cálculo de uma das
# #seguintes médias de acordo a letra digitada pelo usuário
import math as m
op= (input("Escolha a operacao desejada:\n A-Geometrica,\n B-Ponderada,\n C-Harmonica,\n D-Aritmetica.\n Insira aqui:\n"))

if (op=="A"):

    n1=int(input("Insira um numero inteiro positivo:\n"))
    n2=int(input("Insira um numero inteiro positivo:\n"))
    n3=int(input("Insira um numero inteiro positivo:\n"))
    geom= m.cbrt(n1*n2*n3)
    med= "Geometrica"
    reslt = (geom)

elif (op=="B"):

    n1=int(input("Insira um numero inteiro positivo:\n"))
    n2=int(input("Insira um numero inteiro positivo:\n"))
    n3=int(input("Insira um numero inteiro positivo:\n"))
    pond= n1+2*n2+3*n3/6
    med= "Ponderada"
    reslt = (pond)
    
elif (op=="C"):

    n1=int(input("Insira um numero inteiro positivo:\n"))
    n2=int(input("Insira um numero inteiro positivo:\n"))
    n3=int(input("Insira um numero inteiro positivo:\n"))
    harm=1/(1/n1 + 1/n2 + 1/n3)
    med= "Harmonica"
    reslt = (harm)

elif (op=="D" or "d"):

    n1=int(input("Insira um numero inteiro positivo:\n"))
    n2=int(input("Insira um numero inteiro positivo:\n"))
    n3=int(input("Insira um numero inteiro positivo:\n"))
    arit=n1+n2+n3/3
    med= "Aritmetica"
    reslt = (arit)

    
    print("A medida %s" %(med), "e: %s\n" %(reslt))

else:
    print("A opcao escolhida e invalida!!!!")