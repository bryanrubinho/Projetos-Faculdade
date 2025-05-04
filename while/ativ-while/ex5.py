#5) Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2
#deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até
#N.

while True:
    num=int(input("Insira um valor maior que 2:\n"))
    if (num>2):
        break
    else:
        print("Insira outro valor\n")
    
for n in range(2, num +1): #2 pq comeca no 2 e o num +1 atribui o valor inserido a variavel num onde vai ficar o valor que sera usado para as operacoes no for
    qdd= n **2
    cb= n **3

print("O quadrado e:\n %d \nO cubo e:\n %d"%(qdd, cb))
     

    
    
