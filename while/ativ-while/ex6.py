#6)Elaborar um programa que solicita um número (entre 10 a 15). Se o usuário digitar um número
#diferente, o programa deve mostrar a mensagem “Entrada inválida” e solicitar um número
#novamente. Se digitar correto o programa deve mostrar a raiz quadrada desse número e
#.
import math as m
while True:
    num= int(input("Insira um numero de 10 a 15:\n"))
    if (num>=10) and (num<=15):
        raiz= m.sqrt(num)
        print("A raiz quadrada desse numero e:\n %f" % (raiz))
        break
    else:
        print("Entrada inválida")