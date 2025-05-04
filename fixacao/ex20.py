#20) Elaborar um programa que receba o número de horas trabalhadas e o valor do salário mínimo.
#Calcule e mostre o salário a receber seguindo as regras abaixo:
#a) o valor da hora trabalhada vale a metade do salário mínimo;
#b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora
#trabalhada;
#c) o imposto equivale a 3% do salário bruto;
#d) o salário a receber equivale ao salário bruto menos o imposto.

#entrada
ht = float(input("Insira as horas trabalhadas:\n"))
s_min= float(input("Insira o salário minimo:\n"))
#processo
v_ht= s_min/2
s_bruto = ht *v_ht
imp= s_bruto * 3/100
s_liquido = s_bruto-imp
#saida
print("O valor da hora trabalhada é: %f", v_ht)
print("O valor do salário bruto é: %f", s_bruto)
print("O valor do imposto é: %f", imp)
print("O salário liquido é: %0.1f", s_liquido)
