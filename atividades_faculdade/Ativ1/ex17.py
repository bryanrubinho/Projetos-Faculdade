#17) Elaborar um programa que leia a idade de uma pessoa expressa em anos, meses e dias e
#mostre-a expressa apenas em dias

#entrada
anos= int(input("Insira  a sua idade em anos\n"))
meses = int(input("Insira a sua idade em meses\n"))
dias = int(input("Insira sua idade em dias\n")) 
#processo
d= (anos*365) + (meses*30)
#saida
print ("A idade em dias é:", d)