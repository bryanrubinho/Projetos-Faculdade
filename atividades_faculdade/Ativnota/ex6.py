#6)Elaborar um programa que mostre ao usuário um menu com 4 opções de operações 
#matemáticas (1- soma, 2- subtração, 3- multiplicação e 4- divisão). Após o usuário escolher uma 
#das opções, o programa deve solicitar dois números e realiza a operação escolhida. Logo em 
#seguida, o programa deve mostrar qual foi conta realizada e qual o resultado




op=(input("Qual operacao deseja realizar?\n 1- soma,\n 2- subtração,\n 3- multiplicação,\n 4- divisão:\n"))

if (op=="1"):
    n1=int(input("Insira um numero:\n"))
    n2=int(input("Insira um numero:\n"))
    soma= n1+n2
    classif=soma
elif (op=="2"):
    n1=int(input("Insira um numero:\n"))
    n2=int(input("Insira um numero:\n"))
    sub= n1-n2
    classif=sub
elif (op=="3"):
    n1=int(input("Insira um numero:\n"))
    n2=int(input("Insira um numero:\n"))
    mp= n1*n2
    classif=mp
elif (op=="4"):
    n1=float(input("Insira um numero:\n"))
    n2=float(input("Insira um numero:\n"))
    dv= n1/n2
    classif=dv
print("O Resultado e:\n %s" %(classif))
