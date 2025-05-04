#2) Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana
#correspondente. O programa deve repetir até que o usuário digite um número fora desse
#intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número
#inválido”

numero=int(input("Insira um numero:\n"))
while (numero<7):
    if numero == 1:
        print("Segunda-Feira")
        numero=int(input("Insira um numero:\n"))
    elif numero ==2:
        print("Terça-Feira")
        numero=int(input("Insira um numero:\n"))
    elif numero ==3:
        print("Quarta-Feira")
        numero=int(input("Insira um numero:\n"))
    elif numero ==4:
        print("Quinta-Feira")
        numero=int(input("Insira um numero:\n"))
    elif numero ==5:
        print("Sexta-Feira")
        numero=int(input("Insira um numero:\n"))
    elif numero ==6:
        print("Sábado")
        numero=int(input("Insira um numero:\n"))
    elif numero ==7:
        print("Domingo")
        numero=int(input("Insira um numero:\n"))
else:
        print("Inválido")
        