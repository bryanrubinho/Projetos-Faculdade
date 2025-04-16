#9)Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal
#de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler
#qual a condição de pagamento escolhida e efetuar o cálculo adequado.   
#1)à vista em dinheiro ou cheque, recebe 10% de desconto
#2)à vista no cartão de crédito, recebe 15% de desconto
#3)Em duas vezes, preço normal de etiqueta sem juros
#4)Em mais de duas vezes, preço normal de etiqueta mais juros de 10%

pre_etiq=float(input("Insira o preço de etiqueta:\n"))

cond_pag= input("Insira a condição de pagamento\n")
desc_avista= 10/100

if (cond_pag == "AvDin"):
    d10=pre_etiq-(pre_etiq*0.10)
    print("O valor total com desconto é\n", d10)
elif (cond_pag == "AvCrt"):
    d15=pre_etiq-(pre_etiq*0.15)
    print("O valor total com 15% de desconto é: \n ", d15)
elif(cond_pag == "DVZ"):
    dvz= pre_etiq / 2 
    tl= pre_etiq
    print("O valor em duas vezes é:\n", dvz, "\n O total é:\n", tl)
elif(cond_pag == "MVZ"):
    vezes= int(input("Insira a quantidade de vezes:\n"))
    
    mvz = pre_etiq+(pre_etiq*0.10)
    print("O valor em:", vezes, "vezes, é:\n", mvz)


