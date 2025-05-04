#10)Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida
# pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista.

lista=[]

while len(lista)<15:
    num=float(input("Insira 15 valores:\n" f"Valor {len(lista)+1} de 15:\n"))

    if num not in lista:
        lista.append(num)
        print("Nao existem numeros repitidos!!!", lista)
    else:
        print("Invalido numeros repetidos!")
        

