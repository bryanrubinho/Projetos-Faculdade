# 9)Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve
# preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário que digite dois
# números. Esses números devem corresponder a posições na lista (caso contrário solicite um novo valor).
# Após inserir os dois números o programa deve exibir a soma dos elementos das
# duas posições da lista.

lista=[]


while len(lista) < 25:
    num = float(input("digite 25 valores na lista:\n" f"lista {len(lista)+1} de 25:")) #{len(lista)+1} mostra qual a posicao ele vai digitar o valor exemplo 3 de 25
    lista.append(num)
num1=-1
while (num1<0) or (num1>25):
    num1=int(input("Insira uma posicao (de 1 a 25):\n"))
num2=-1     
while (num2<0) or (num2>25):
    num2=int(input("Insira uma posicao (de 1 a 25):\n"))
    soma=lista[num1]+ lista[num2]
    print("A soma da do item:\n %d \ne o item:\n %d \no total e:\n %d" % (lista[num1], lista[num2],soma))
    