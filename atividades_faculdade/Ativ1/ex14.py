#14)Elaborar um programa que leia uma temperatura em graus Celsius e deve converter em graus
#Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5, sendo F a temperatura em Fahrenheit e C
#a temperatura em Celsius. Exibir a temperatura em Fahrenheit.

#entrada
c= int(input("Insira a temperatura em graus Celcius:\n"))
#processo
f=(9*c+160)/5
#saida
print("A temperatura em Fahrenheit é", f)