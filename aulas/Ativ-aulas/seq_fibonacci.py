anterior =0  
atual=1      #as duas variaveis definem espaços no for ent ja temos 2 espaços e queremos o 5
lista=[]   #abertura de lista vazia
lista.append(anterior)  #adição de variaveis na lista 
lista.append(atual)  #adição de variaveis na lista
lista.reverse()
limite= int(input("Digite o elemento Desejadao:\n"))
for n in range(limite -2):   #o limite-2 subtrai as duas variaveis a cima pois elas sao os dois primeiros valores da lista
    futuro = atual+anterior  #o futuro é igual ao numero atual somado ao anterior para calcular a fibonacci
    anterior = atual #faz o numero anterior mudar e virar atual
    atual = futuro   #a variavel atual é igual ao valor do furturo
    lista.append(futuro) #adiciona o valor que a variavel futuro vai armazenar na lista
    print(lista)  #exibe a lista comn os 5 itens pedidos( as duas variaveis e o que foi incluido no range)  
   
    print("O %d elemento da sequência fibonacci é: %d" % (limite, futuro))
