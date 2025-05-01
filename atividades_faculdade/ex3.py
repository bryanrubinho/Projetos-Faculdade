num= 1
lista=[]

while(num!=0):
    num=float(input("Insira um número:\n"))
    lista.append(num)
    soma=sum(lista)
    media = soma/len(lista) #len quantidade de elementos na lista, sum é a soma dos elementos
print(lista)
print(soma)
print(media)

    
    

    
