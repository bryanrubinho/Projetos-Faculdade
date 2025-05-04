
#6)Elaborar um programa que receba o salário de um funcionário e o percentual de aumento, calcule
#e mostre o valor do aumento e o novo salário.

#entrada
salario= int(input("Insira o salário\n"))
aumento= int(input("Insira a % de aumento\n"))
#processo
porcentagem = salario*aumento/100
salario_novo = salario+porcentagem
#saida
print("O valor do aumento é:\n", porcentagem)
print ("O Novo Salário é R$\n", salario_novo)