                        #conceitos de lista


#moveis.sort() #Ordea em ordem alfabetica

#moveis.reverse()#Ordem decrescente
#//
#codigo com adiçao e apresentação separada
moveis=["cama", "mesa","cadeira ","armario" ]
valor=moveis [:] #[:] separa oq eu faço na lista moveis e oque e apresentado na valor

moveis.append("comoda")

print(moveis)
print (valor)

#//

#//
#valor aparece com a lista toda atualizada pois nao ha separação na lista
#ou seja copia  a lista em toda sua instancia
moveis=["cama", "mesa","cadeira ","armario" ]
valor=moveis
moveis.append("comoda")
print (valor)
#//
#SPLIT(:)SEPARA COMO DADOS
#SPLIT(.) SEPARA COMO INFORMAÇÃO

texto = "www.eupoderiaterestudadomais.com"
print(texto.split("."))  #separa nos pontos ex www

print("13:15:45".split(":")) #separa pelos dois pontos":"

hora, minuto, segundo = "13:15:45".split(":")
print(hora, minuto, segundo) #separa pelos dois pontos e atribui cada um a uma variavel

#range nao ocupa espaço de memoria, tem inicio fim passo, 
# start opcional se eu nao colocar é 0
# stop obrigatorio um numero inteiro especificado em qual posição parar
#step opcional se nao especificado é 1
 

#for variavel in sequencia :
    #comandos a serem repitidos
    #na sequencia sabemos quando inicia e quando termina
    #comandos após o for

for n in range(1, 31, 2):
   print(n)

x=range(1,31,2)
for n in x:
    print(n)

moveis=["cama", "mesa","cadeira ","armario" ]
for x in moveis:
    print(x)