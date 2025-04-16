#5) Elaborar um programa para automatizar o caixa de uma lanchonete. Este algoritmo deve ler o 
#código do item pedido, a quantidade e calcular o valor a ser pago por aquele lanche. No final o 
#programa deve mostrar o total a ser pago. O cardápio da lanchonete é o seguinte


coditem= float(input("Insira o código do produto:\n"))
qnt_it= float(input("Insira a quantidade de produto:\n"))

if (coditem==100):
    cq= "cachorro quente"
    ttl= qnt_it*3.5
    print("O preço dos produtos é R$: %s",(ttl))
elif (coditem==101):
    cq= "Bauru Simples"
    ttl= qnt_it*3.8
    print("O preço dos produtos é R$: %s",(ttl))
elif (coditem==102):
    cq= "Bauru c/ ovo"
    ttl= qnt_it*4.5
    print("O preço dos produtos é R$: %s",(ttl))
elif (coditem==103):
    cq= "Hamburguer"
    ttl= qnt_it*4.7
    print("O preço dos produtos é R$: %s",(ttl))
elif (coditem==104):
    cq= "Cheeseburguer"
    ttl= qnt_it*5.30
    print("O preço dos produtos é R$: %s",(ttl))
elif (coditem==105):
    cq= "Refrigerante"
    ttl= qnt_it*4.00
    print("O preço dos produtos é R$: %s",(ttl))