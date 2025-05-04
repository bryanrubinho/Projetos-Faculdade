#lista de produtos definida
cod=[1,2,3,4,5,6 ]
esp=["Hot-Dog", "X-burguer", "X-egg", "X-Tudo", "Refri", "Água"]
vlr_unt=[20.00,28.00,32.00,40.00,8.00,5.00]

#escolha se deseja fazer pedido
nv_pdd=(input("Você deseja fazerum novo pedido? [S/N]\n"))

if (nv_pdd=="S") or (nv_pdd=="s"):

    #Inserir o nome do cliente
    ncliente=(input("Insira o nome do cliente:\n"))


    #Exibição de lista em menu
    menu=[cod[0], esp[0], "R$" + str(vlr_unt[0])]
    print(menu)
    menu=[cod[1], esp[1], "R$" + str(vlr_unt[1])]
    print(menu)
    menu=[cod[2], esp[2], "R$" + str(vlr_unt[2])]
    print(menu)
    menu=[cod[3], esp[3],"R$" + str(vlr_unt[3])]
    print(menu)
    menu=[cod[4], esp[4], "R$" + str(vlr_unt[4])]
    print(menu)
    menu=[cod[5], esp[5],  "R$" + str(vlr_unt[5])]
    print(menu)
    
escolha_c = int(input("Escolha a opção que deseja:\n"))
qnt= int(input("Quantos deseja:\n"))


if (escolha_c>0) and (escolha_c<6):
    if escolha_c == 1:
        x=0
        vlr_ttl= vlr_unt[x]*qnt
        pedido=[ncliente, esp[x], vlr_unt[x], qnt, vlr_ttl]
        print(pedido)
    elif escolha_c==2:
        x=1
        vlr_ttl= vlr_unt[x]*qnt
        pedido=[ncliente, esp[x], vlr_unt[x], qnt,vlr_ttl]
        print(pedido)
    elif escolha_c==3:
        x=2
        vlr_ttl= vlr_unt[x]*qnt
        pedido=[ncliente, esp[x], vlr_unt[x], qnt,vlr_ttl]
        print(pedido)
    elif escolha_c==4:
        x=2
        vlr_ttl= vlr_unt[x]*qnt
        pedido=[ncliente, esp[x], vlr_unt[x], qnt,vlr_ttl]
        print(pedido)
    elif escolha_c==5:
        x=4
        vlr_ttl= vlr_unt[x]*qnt
        pedido=[ncliente, esp[x], vlr_unt[x], qnt,vlr_ttl]
        print(pedido)
    elif escolha_c==6:
        x=5
        vlr_ttl= vlr_unt[x]*qnt
        pedido=[ncliente, esp[x], vlr_unt[x], qnt,vlr_ttl]
        print(pedido)
    else:
        print("Opção Inválida")

        