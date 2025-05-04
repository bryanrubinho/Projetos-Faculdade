#5)Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando
#um reajuste de 15%.

#entrada
saldo=int(input("Digite o saldo\n"))
#processamento
reajuste=1.15
novo_saldo= reajuste*saldo
#saida
print("o novo saldo é R$:\n", novo_saldo)