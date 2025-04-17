#7) Elaborar um algoritmo que leia 10 números. Logo após, deve exibir o menor valor lido e o maior
#valor lido.
num= float(input("Insira um valor\n"))
maior=num
menor=num
for x in range(10):  

    num= float(input("Insira um valor\n"))

    if num > maior:
        maior = num
    if num < menor :
        menor = num

print("\nMenor valor:", menor)
print("Maior valor: ", maior)




