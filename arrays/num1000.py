#8) Elaborar um algoritmo que some todos os números inteiros abaixo de 1000 que são múltiplos de
#3 ou 5

num=[]
soma=0


for x in range(10):
    num=int(input("Insira um numero:\n"))

    if (num<1000) and (num % 3 == 0) or (num % 5 == 0):
        soma += num
        print("O valor e menor que 1000, a soma dos divisiveis por 3 ou 5 e:\n", soma)
    else:
        print("Invalido")
        
  
 
