#4) Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar
#o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80,
#quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário

numeros=[] #abertura de lista
maior=0
menor=0
while True:
    num=float(input("Insira um numero inteiro (Digite 100 para parar): \n")) #solicitacao de numeros
    if(num==100):
        break #parar o codigo
    numeros.append(num) #adiciona os numeros na lista
    if (num>80):   #se for maior q 80  ele soma o valor aos da variavel
        maior+= 1 
    elif (num<10):  #faz o mesmo se for menor
        menor+= 1 
    else:
        print("invalido")
if len(numeros)>0: # se os numeros da lista forem maiores q 0 realiza a operacao
        media=sum(numeros) / len(numeros) #divide e soma as listas
else:
        media=0
print("valores acima de 80:\n %d" % (maior))
print("Valores abaixo de 10:\n %d" % (menor))
print("A media dos numeros e:\n %0.2f" % (media))

