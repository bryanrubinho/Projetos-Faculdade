#4)Elaborar um programa que calcule o consumo médio de um automóvel (medido em km/l), dado
#que são conhecidos a distância total percorrida e o volume de combustível consumido para
#percorrê-la (medido em litros).

#entrada
cons_medio= int(input("Insira a distancia percorrida\n"))
litros= int(input("Insira os Litros consumidos\n"))
#processamento
media=cons_medio/litros
#saida
print("A media de é\n", media, "km/l")