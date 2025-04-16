#4)Elabore um algoritmo que lê um numero inteiro entre 1 e 7 e exibe o dia da semana correspondente. 
#Caso o usuário digite um numero fora desse intervalo, o algoritmo mostra uma mensagem informando "Número Inválido"


n1 = int(input("Insira um número de 1 a 7:\n"))
if (n1==1):
        print("Domingo")
elif(n1==2):
    print("Segunda-feira")
elif (n1==3):
    print("Terça-Feira ")
elif (n1==4):
    print("Quarta-Feira")
elif (n1==5):
    print("Quinta-Feira")
elif (n1==6):
    print("Sexta-Feira")
elif (n1==7):
    print("Sábado")
else:
    print("Número Inválido")
