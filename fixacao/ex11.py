#11) Elaborar um programa que calcule a aceleração de um corpo em movimento conhecendo-se
#as velocidades inicial e final, e o intervalo de tempo medido (a = (v2 –v1)/∆t). Exibir o resultado.

#entrada
v1=float(input("Insira a Velocidade Inicial\n"))
v2= float(input("Insira a Velocidade Final\n"))
int_temp=float(input("Insira o intervalo de tempo\n"))
#processo
aceleracao = (v2 - v1)/ int_temp
#saida
print("a aceleração é:", aceleracao)
