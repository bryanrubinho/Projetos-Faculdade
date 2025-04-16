#2 Elabore um algoritmo que calcule a soma de dois números quaisquer e apresente na tela o resultado dessa soma. Caso a soma seja superior a 30 indicar qual é o maior valor entre eles
n1=float(input("Digite um numero:\n"))
n2=float(input("Digite um outro numero:\n"))
soma=(n1+n2)
print("a soma é:", soma)
if(soma>30)and(n1>n2):
    print("o maior número é: ", n1)
else:
    print("o número não é maior que 30", n2)