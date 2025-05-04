
#19)Elaborar um programa que calcule o salário líquido de um funcionário, exibindo no final o nome,
#telefone e o salário líquido, considerando:
#a)os dados do funcionário: nome, RG e telefone.
#b)salário bruto de R$ 2500,00
#c)descontos de R$ 300,00

#entrada
nome = (input("Insira seu nome:\n"))
telefone = (input("Insira seu telefone:\n"))
rg = (input("Insira seu rg:\n"))
s_bruto = 2500
d = 300
#processo
s_liquido= s_bruto-d
#saida
print("o salário liquido de",nome,"do rg", rg, "e portadora do telefone", telefone, "é:", s_liquido)
