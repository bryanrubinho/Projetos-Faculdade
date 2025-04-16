#7)Elaborar um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e
#mostre:
#- A idade desta pessoa hoje;
#- A idade desta pessoa em 2035.

#entrada
ano_atual= int(input("Insira o ano atual\n"))
ano_nasc= int(input("Insira o ano de seu nascimento\n"))
#processo
idade= ano_atual - ano_nasc 
idade_2035= idade+10
#saida
print("A idade atual é:\n", idade)
print("A idade em 2035 é:\n", idade_2035)
