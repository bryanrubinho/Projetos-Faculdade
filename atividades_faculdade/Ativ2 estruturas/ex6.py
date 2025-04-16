6# Faça um algoritmo que leia o nome, o sexo, o estado civil de uma pessoa. Caso sexo seja "F" e estado civil seja "CASADA", solicitar o tempo de casada (anos).
nome=(input("Digite seu nome:\n"))
sexo=(input("Digite seu sexo:\n"))
estado=(input("Digite seu estado civil:\n"))


if(sexo== "f")and(estado=="casada"):
    print(input("quantos anos casada?\n"))
else:
    print("obrigado pelas infos")