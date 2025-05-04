#7) Elaborar um programa para automatizar o caixa de uma lanchonete. Este programa deve ler o
#código do item pedido, a quantidade e somar para calcular o valor a ser pago. O programa
#termina quando o código for 0 (zero). 

#lista de produtos definida
cod=[1,2,3,4,5,6]
esp=["Cachorro Quente", "bauru Simples", "Bauru c/ ovo", "Hamburguer", "Cheeseburguer", "Refrigerante"]
vlr_unt=[3.50,3.80,4.50,4.70,5.30,4.00]

#escolha se deseja fazer pedido
while True:
    nv_pdd=(input("Você deseja fazer um novo pedido? [S/N]\n"))

    if (nv_pdd.upper()=="S"):
        
        print("Menu:")
        for n in range(len(cod)):
            print(cod[n], esp[n], vlr_unt[n])

        esc_cod=int(input("Insira o codigo o pedido:\n"))
        if cod==0:
            print("Obrigado, sistema encerrando.\n Volte Sempre!!!")
            break
        elif esc_cod in cod:
            qnt=float(input("Insira a quantidade do pedido:\n"))
            codp=cod.index(esc_cod)
            vlr_ttl = vlr_unt[codp] * qnt
            pedido=[esp[codp],f"R${vlr_unt[codp]:.2f}", qnt,f"Total: R$ {vlr_ttl:.2f}"]
            print("O seu pedido e:\n", pedido)
        else:
            print("Opcao Invalida.")
    elif (nv_pdd.upper()=="N"):
        print("Encerrando sistema... Obrigado!")
        break
    else:
        print("Opcao Invalida, por favor escolha S ou N")
 