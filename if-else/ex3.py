#3) Elaborar um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
#a seguir, verifique e mostra qual a classificação dessa pessoa.

alt= float(input("Insira a altura:\n"))
peso= float(input("Insira o peso:\n"))

if (alt<1.20) and ( peso<60):
    print("Classificação A")
elif (peso>=60) and (peso<=90):
    print("Classificação D")
elif (peso>90):
    print("Classificação G")
    
    
elif (alt>=1.20) or (alt<=1.70) and (peso<60):
    print("Classificação B")
elif (peso>=60)  and (peso<=90):
    print("Classificação E")
elif (peso>90):
    print("Classificação H")
    
    
elif (alt>1.70) or (peso<60):
    print("Classificação C")
elif (peso>=60)  and (peso<=90):
    print("Classificação F")
elif (peso>90):
    print("Classificação I")
    
    