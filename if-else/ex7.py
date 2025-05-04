#7) Elaborar um programa que receba três valores (A, B, C). O programa deve verificar se eles 
#podem ser valores dos lados de um triângulo, e se forem, se é um triângulo escaleno, equilátero 
#ou isóscele, considerando os seguintes conceitos:
#• O comprimento de cada lado de um triângulo é menor do que a soma dos outros
#dois lados.
#• Chama-se equilátero o triângulo que tem três lados iguais.
#• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
#• Recebe o nome de escaleno o triângulo que tem os três lados diferente

a=int(input("Insira um numero:\n"))
b=int(input("Insira um numero:\n"))
c=int(input("Insira um numero:/n"))

if(a + b > c )and (a + c > b )and (b + c > a):
    print("Os 3 lados formam um triangulo!\n")
elif (a == b ) and (a == c):
    print("Equilatero!")
elif (a==b) or (a==c) or (b==c):
    print("Isósceles!")
elif (a!=b!=c):
    print("Escaleno!")
else:
    print("Nao e um triangulo!")



