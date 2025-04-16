#2) Elaborar um programa que leia a distancia em km e a quantidade de litros de gasolina 
#consumidos por um carro em um percurso, calcule o consumo em Km/l e mostre uma mensagem 
#de acordo com a tabela abaixo


d_km= int(input("Insira a distancia em km:\n"))
qnt_l= int(input("Insira a quantidade consumida em Litros:\n"))

consumo=d_km/qnt_l

if (consumo<8):
    print("Venda o Carro!")
elif (consumo>=8) and (consumo<=14):
    print("Econômico!")
elif (consumo>14):
    print("Super econômico!")
    